"""Mechanical field-layout normalization; never invent billing evidence or judgments."""
from copy import deepcopy

def normalize(value):
    result=deepcopy(value)
    cost=result.get('service_cost')
    changes=[]
    if isinstance(cost,dict) and isinstance(cost.get('sources'),list):
        sources=cost['sources']
        def valid(item):
            if isinstance(item,str):return bool(item.strip())
            if not isinstance(item,dict):return False
            key='url' if 'url' in item else 'ref'
            allowed={'url','note'} if key=='url' else {'ref','type','note'}
            return (set(item)<=allowed and isinstance(item.get(key),str) and bool(item[key].strip())
                    and isinstance(item.get('note',''),str) and isinstance(item.get('type',''),str))
        def source_text(item):
            if isinstance(item,str):return item
            prefix='['+item['type']+'] ' if item.get('type') else ''
            return prefix+item.get('url',item.get('ref'))+(' — '+item['note'] if item.get('note') else '')
        if sources and all(valid(item) for item in sources) and any(isinstance(item,dict) for item in sources):
            cost['sources']=[source_text(item) for item in sources]
            changes.append('Joined existing service_cost.sources URL or typed reference objects into source strings; all supplied values retained')
    fields=('rule','observed','evidence')
    if (isinstance(cost,dict) and cost.get('kind')=='confirmed_free'
            and isinstance(cost.get('applicability'),str) and cost['applicability'].strip()
            and 'observed' not in cost
            and all(isinstance(cost.get(k),str) and cost[k].strip() for k in ('rule','evidence'))):
        cost['observed']=cost.pop('applicability')
        changes.append('Renamed existing string service_cost.applicability to observed; value unchanged')
    if (isinstance(cost,dict) and cost.get('kind')=='confirmed_free'
            and 'applicability' not in cost
            and all(isinstance(cost.get(k),str) and cost[k].strip() for k in fields)):
        cost['applicability']={k:cost.pop(k) for k in fields}
        changes.append('Moved existing service_cost.rule/observed/evidence into service_cost.applicability; values unchanged')
    if isinstance(cost,dict) and cost.get('kind')=='confirmed_free':
        applicability=cost.get('applicability')
        evidence=applicability.get('evidence') if isinstance(applicability,dict) else None
        if (isinstance(evidence,list) and evidence
                and all(isinstance(item,str) and item.strip() for item in evidence)
                and all(isinstance(applicability.get(k),str) and applicability[k].strip() for k in ('rule','observed'))):
            applicability['evidence']='\n'.join(evidence)
            changes.append('Joined existing service_cost.applicability.evidence references with newlines; references unchanged')
    if (changes and 'note' not in cost and isinstance(cost.get('applicability'),dict)
            and isinstance(cost['applicability'].get('rule'),str)):
        cost['note']=cost['applicability']['rule']
        changes.append('Copied the existing free-rule text into service_cost.note; no billing fact added')
    return result,changes
