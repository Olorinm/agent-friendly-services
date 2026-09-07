import json, urllib.request, urllib.error, pathlib, datetime, re
ROOT=pathlib.Path('evidence')
BASE='https://mcp.kiwi.com'
session=None

def call(name,payload):
 global session
 headers={'Accept':'application/json, text/event-stream','Content-Type':'application/json'}
 if session: headers['Mcp-Session-Id']=session
 (ROOT/(name+'-request.json')).write_text(json.dumps({'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'POST','url':BASE,'body':payload},indent=2))
 req=urllib.request.Request(BASE,data=json.dumps(payload).encode(),headers=headers,method='POST')
 try:
  response=urllib.request.urlopen(req,timeout=90)
 except urllib.error.HTTPError as e:
  response=e
 status=response.status
 session=response.headers.get('Mcp-Session-Id',session)
 data=response.read().decode()
 # Never persist credentials, even if included in a returned URL or JSON field.
 safe=re.sub(r'(?i)([?&](?:[^=&\s\"\\]*token|api_?key|auth|signature)=)[^&\s\"\\]*',r'\1[REDACTED]',data)
 safe=re.sub(r'(?i)(\"(?:access_token|refresh_token|id_token|token|api_key|authorization|cookie|set-cookie)\"\s*:\s*\")[^\"]*',r'\1[REDACTED]',safe)
 (ROOT/(name+'-response.txt')).write_bytes(safe.encode())
 (ROOT/(name+'-metadata.json')).write_text(json.dumps({'status':status,'content_type':response.headers.get('Content-Type'),'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'response_redacted':safe!=data},indent=2))
 print(name,status,safe[:16000],flush=True)
 return data

if __name__=='__main__':
 call('initialize',{'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2024-11-05','capabilities':{},'clientInfo':{'name':'flight-evidence-client','version':'1.0'}}})
 call('initialized',{'jsonrpc':'2.0','method':'notifications/initialized'})
 call('tools-list',{'jsonrpc':'2.0','id':2,'method':'tools/list','params':{}})
