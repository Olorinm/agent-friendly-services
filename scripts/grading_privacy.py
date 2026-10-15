"""Remove explicitly registered credentials from grader copies, retaining originals."""
import base64
import hashlib
import json
from pathlib import Path
from urllib.parse import quote, quote_plus
from credential_facts import document as credential_document, decoded_facts


def secret_forms(value):
    return [value.encode(),json.dumps(value,ensure_ascii=True)[1:-1].encode(),
            json.dumps(value,ensure_ascii=False)[1:-1].encode(),
            quote(value,safe='').encode(),quote_plus(value).encode(),
            base64.b64encode(value.encode()),base64.urlsafe_b64encode(value.encode())]


def secrets_for(directory):
    path=Path(directory)/'private-secrets.json'
    values=json.loads(path.read_text()) if path.exists() else []
    if not isinstance(values,list) or any(not isinstance(v,str) or len(v)<8 for v in values):
        raise ValueError('Grading secrets must be explicit strings of at least eight characters')
    return values


def redact_tree(root, secrets):
    root=Path(root)
    variants=set()
    credential_variants={}
    for value in secrets:
        forms=secret_forms(value)
        variants.update(forms)
        facts=decoded_facts(value)
        if facts is not None:credential_variants[facts['credential_sha256']]=forms
    variants=sorted(variants,key=len,reverse=True)
    if not variants:return []
    changed=[]
    files=list(root.rglob('*'))
    # Reject dangerous paths before modifying any content.
    for path in files:
        if path.is_symlink():raise ValueError('Grading copy must not contain symlinks')
        if any(v in str(path.relative_to(root)).encode() for v in variants):
            raise ValueError('Credential occurs in a grading filename; inspect before dispatch')
    pending=[]
    for path in files:
        if not path.is_file():continue
        original=path.read_bytes();safe=original
        for value in variants:safe=safe.replace(value,b'[SERVICE_SECRET]')
        if safe==original:continue
        format_note=None
        if path.suffix=='.json':
            try:json.loads(original)
            except (ValueError,UnicodeDecodeError):
                # Captured artifacts may contain JSON followed by curl's HTTP
                # status, or arbitrary text. Their suffix is not a format
                # contract. Retain those bytes and their original provenance.
                format_note='Original artifact is not a single JSON document; byte-preserving text/binary redaction.'
            else:json.loads(safe)  # Valid JSON must remain valid after redaction.
        pending.append((path,original,safe,format_note))
    # Complete validation before any write, so a later rejection cannot leave
    # partially redacted inputs without a complete provenance report.
    for path,original,safe,format_note in pending:
        path.write_bytes(safe);path.chmod(0o600)
        info={'path':str(path.relative_to(root)),
              'original_sha256':hashlib.sha256(original).hexdigest(),
              'redacted_sha256':hashlib.sha256(safe).hexdigest()}
        linked=[key for key,forms in credential_variants.items() if any(v in original for v in forms)]
        if linked:info['registered_credential_sha256']=sorted(linked)
        if format_note:info['format_note']=format_note
        changed.append(info)
    return changed


def protect_grading(directory):
    directory=Path(directory);grade=directory/'grading-input'
    secrets=secrets_for(directory)
    facts=credential_document(secrets)
    facts_path=grade/'credential-facts.json'
    if facts is not None:
        raw=json.dumps(facts,ensure_ascii=False,indent=2)+'\n'
        if any(v in raw.encode() for secret in secrets for v in secret_forms(secret)):
            raise ValueError('Credential facts overlap a registered secret; inspect before dispatch')
        if facts_path.exists() or facts_path.is_symlink():
            if facts_path.is_symlink() or facts_path.read_text()!=raw:
                raise ValueError('Registered credential facts changed; inspect before dispatch')
    elif facts_path.exists() or facts_path.is_symlink():
        raise ValueError('Credential facts have no matching registered source')
    changed=redact_tree(grade,secrets)
    if facts is not None and not facts_path.exists():
        facts_path.write_text(raw);facts_path.chmod(0o600)
    if changed:
        report={'notice':'Controller verified raw source hashes before copying. These grader files redact registered service secrets; raw originals remain private. Source locators refer to originals, not the redacted bytes. Redacted credentials cannot be used for independent service access.',
                'files':changed}
        (grade/'privacy-redactions.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        with (grade/'prompt.txt').open('a') as stream:
            stream.write('\n本次副本包含已登记服务凭据的脱敏，见 privacy-redactions.json。原始 source 哈希已由总控核验并保留，副本标记 [SERVICE_SECRET] 不是可用凭据；不能据此补做需要执行者权限的任务。\n')
    if facts is not None:
        notice='\n凭据的非秘密字段见 credential-facts.json；来源关联见 privacy-redactions.json 的 registered_credential_sha256。仅登记或解码不证明实际使用、签名有效、当前授权、真实传输方式或费用；缺少来源关联时保留未知。该文件及副本不得公开。\n'
        prompt=grade/'prompt.txt'
        if notice not in prompt.read_text():
            with prompt.open('a') as stream:stream.write(notice)
    return changed
