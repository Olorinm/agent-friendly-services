from kiwi_probe import call
from concurrent.futures import ThreadPoolExecutor, as_completed

queries=[('mxp-ams','MXP','AMS'),('lin-ams','LIN','AMS'),('bgy-ein','BGY','EIN')]
def run(query):
 name,origin,destination=query
 return call('search-'+name,{'jsonrpc':'2.0','id':3,'method':'tools/call','params':{'name':'search-flight','arguments':{'flyFrom':origin,'flyTo':destination,'departureDate':'25/09/2026','departureDateFlexDays':0,'adults':1,'children':0,'infants':0,'cabinClass':'M','currency':'EUR','sort':'price'}}})
with ThreadPoolExecutor(max_workers=3) as pool:
 jobs={pool.submit(run,q):q for q in queries}
 for job in as_completed(jobs):
  try: job.result()
  except Exception as exc: print(jobs[job],type(exc).__name__,str(exc),flush=True)
