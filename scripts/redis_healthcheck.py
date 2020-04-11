import sys
import requests
import json
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import redis

redis_host = sys.argv[1]
redis_port = sys.argv[2]
prometheus_pushgateway_url = sys.argv[3]
alert_name = sys.argv[4]


def redis_check():
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        r.set("redis:test", "pass")
        msg = r.get("redis:test")
        return 99999
    except:
        pass

registry = CollectorRegistry()
g = Gauge(alert_name, 'Last Unix time when change was pushed', registry=registry)
g.set_to_current_time()
g.set(redis_check())
push_to_gateway(prometheus_pushgateway_url, job=alert_name, registry=registry)

print (redis_check())