"""Remove explicitly registered credentials from grader copies, retaining originals."""
import base64
import hashlib
import json
from pathlib import Path
from urllib.parse import quote, quote_plus


def secrets_for(directory):
    path=Path(directory)/'private-secrets.json'
    values=json.loads(path.read_text()) if path.exists() else []
    if not isinstance(values,list) or any(not isinstance(v,str) or len(v)<8 for v in values):
        raise ValueError('Grading secrets must be explicit strings of at least eight characters')
    return values


def redact_tree(root, secrets):
    root=Path(root)
    variants=set()
    for value in secrets:
        variants.update([value.encode(),json.dumps(value,ensure_ascii=True)[1:-1].encode(),
                         json.dumps(value,ensure_ascii=False)[1:-1].encode(),
                         quote(value,safe='').encode(),quote_plus(value).encode(),
                         base64.b64encode(value.encode()),base64.urlsafe_b64encode(value.encode())])
    variants=sorted(variants,key=len,reverse=True)
    if not variants:return []
    changed=[]
    files=list(root.rglob('*'))
    # Reject dangerous paths before modifying any content.
    for path in files:
        if path.is_symlink():raise ValueError('Grading copy must not contain symlinks')
        if any(v in str(path.relative_to(root)).encode() for v in variants):
            raise ValueError('Credential occurs in a grading filename; inspect before dispatch')
    for path in files:
        if not path.is_file():continue
        original=path.read_bytes();safe=original
        for value in variants:safe=safe.replace(value,b'[SERVICE_SECRET]')
        if safe==original:continue
        if path.suffix=='.json':json.loads(safe)  # Fail closed on malformed redaction.
        path.write_bytes(safe);path.chmod(0o600)
        changed.append({'path':str(path.relative_to(root)),
                        'original_sha256':hashlib.sha256(original).hexdigest(),
                        'redacted_sha256':hashlib.sha256(safe).hexdigest()})
    return changed


def protect_grading(directory):
    directory=Path(directory);grade=directory/'grading-input'
    changed=redact_tree(grade,secrets_for(directory))
    if changed:
        report={'notice':'Controller verified raw source hashes before copying. These grader files redact registered service secrets; raw originals remain private. Source locators refer to originals, not the redacted bytes. Redacted credentials cannot be used for independent service access.',
                'files':changed}
        (grade/'privacy-redactions.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        with (grade/'prompt.txt').open('a') as stream:
            stream.write('\n本次副本包含已登记服务凭据的脱敏，见 privacy-redactions.json。原始 source 哈希已由总控核验并保留，副本标记 [SERVICE_SECRET] 不是可用凭据；不能据此补做需要执行者权限的任务。\n')
    return changed
