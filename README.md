**Prometheus**

There are two options that we provide to our developers on how to configure their project. We trigger prometheus repo as part of the CICD process. Whenever a user triggers the project, at the end we have a stage which triggers `configuring monitoring` which takes care of configuring monitoring for the project.

![Image description](https://files.gitter.im/tomarv2/BMMh/Screen-Shot-2020-04-11-at-9.42.27-AM.png)

![Image description](https://files.gitter.im/tomarv2/4hIn/Screen-Shot-2020-04-11-at-9.43.19-AM.png)

***
This repo contains 6 components that we use in our environment to monitor our k8s infrastructure:

- Prometheus (https://github.com/prometheus/prometheus)
- Alertmanager (https://prometheus.io/docs/alerting/alertmanager/)
- Blackbox (https://github.com/prometheus/blackbox_exporter)
- Pushgateway (https://github.com/prometheus/pushgateway)
- Unsee - Decommissioned (https://github.com/cloudflare/unsee) - There has been no commit to this project for a long time
- Elastalert (There is not covered in this repo: https://github.com/Yelp/elastalert)

```
kubectl create configmap prometheus-alertmanager-config-01 --from-file=prometheus-alertmanager/_config/prometheus-alertmanager.yaml --dry-run -o yaml |kubectl replace configmap prometheus-alertmanager-config-01 -f -

kubectl delete job <job_name>

kubectl get jobs

kubectl run demoapp-dev --schedule="* */6 * * *" --restart=OnFailure --env=[AWS_ACCESS_KEY_ID: <set to the key 'access-key' in secret 'nonprod-secret'> AWS_SECRET_ACCESS_KEY: <set to the key 'secret-key' in secret 'nonprod-secret'>] --image=ecr.tomarv2.com/demo/devops/demo:v14 -- /bin/sh -c "su zip -c 'cd ~/; source .bashrc; perl -w /demo.pl'"

kubectl get cronjobs
```