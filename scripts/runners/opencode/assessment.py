"""Mechanical field-layout normalization; never invent billing evidence or judgments."""
from copy import deepcopy

def normalize(value):
    result=deepcopy(value)
    cost=result.get('service_cost')
    changes=[]
    fields=('rule','observed','evidence')
    if (isinstance(cost,dict) and cost.get('kind')=='confirmed_free'
            and 'applicability' not in cost
            and all(isinstance(cost.get(k),str) and cost[k].strip() for k in fields)):
        cost['applicability']={k:cost.pop(k) for k in fields}
        changes.append('Moved existing service_cost.rule/observed/evidence into service_cost.applicability; values unchanged')
    return result,changes
