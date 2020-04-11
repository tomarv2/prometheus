import sys
import requests
import json
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

url = sys.argv[1]
prometheus_pushgateway_url = sys.argv[2]
alert_name = sys.argv[3]
status_check = url + '/_cluster/health?pretty'


def flow_files_queue():
    r = requests.get(status_check, allow_redirects=True)
    a = (json.dumps(r.json(), indent=2))
    resp = json.loads(a)
    #return resp['status']
    try:
        if resp['status'] == 'red':
            return 99999
        else:
            return 0
    except:
        return "unable to get cluster info..."

registry = CollectorRegistry()
g = Gauge(alert_name, 'Last Unix time when change was pushed', registry=registry)
g.set_to_current_time()
g.set(flow_files_queue())
push_to_gateway(prometheus_pushgateway_url, job=alert_name, registry=registry)

#print (flow_files_queue())