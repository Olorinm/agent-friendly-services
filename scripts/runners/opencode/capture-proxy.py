#!/usr/bin/env python3
"""Private loopback-only Coding Plan recorder. No auth headers are logged.

Run as a separate privileged process inside the test container, so the unprivileged
executor cannot read its key or captured prompts. No ports are published.
"""
import argparse
import http.client
import http.server
import json
import os
from pathlib import Path
import time
import uuid

p=argparse.ArgumentParser();p.add_argument('--key',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--port',type=int,default=18181);a=p.parse_args()
os.umask(0o077);a.output.mkdir(parents=True,exist_ok=True)
key=a.key.read_text().strip()

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self,*args): pass
    def do_POST(self):
        if self.path!='/api/coding/paas/v4/chat/completions':
            self.send_error(404);return
        body=self.rfile.read(int(self.headers.get('Content-Length','0')))
        record=a.output/(str(time.time_ns())+'-'+uuid.uuid4().hex[:8]);record.mkdir()
        (record/'request.json').write_bytes(body)
        info={'started_at':time.time(),'path':self.path}
        conn=http.client.HTTPSConnection('open.bigmodel.cn',timeout=150)
        try:
            conn.request('POST',self.path,body,{'Authorization':'Bearer '+key,'Content-Type':'application/json','Accept-Encoding':'identity'})
            res=conn.getresponse();info['status']=res.status
            self.send_response(res.status)
            self.send_header('Content-Type',res.getheader('Content-Type','application/json'))
            self.send_header('Connection','close');self.end_headers()
            with (record/'response.body').open('wb') as out:
                while chunk:=res.read1(65536):
                    out.write(chunk);out.flush()
                    self.wfile.write(chunk);self.wfile.flush()
        except Exception as error:
            info['error']=type(error).__name__
        finally:
            conn.close();info['ended_at']=time.time()
            (record/'meta.json').write_text(json.dumps(info)+'\n')
            self.close_connection=True

http.server.ThreadingHTTPServer(('127.0.0.1',a.port),Handler).serve_forever()
