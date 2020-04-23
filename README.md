# k8s: configuring monitoring

This repo is used to deploy monitoring for a k8s cluster. There are two parts to monitoring a k8s cluster:
- Monitoring the cluster itself
- Monitoring the application(s) deployed on the cluster

I am using 6 components to monitor the k8s infrastructure:

- **Prometheus** - https://github.com/prometheus/prometheus
- **Alertmanager** - https://prometheus.io/docs/alerting/alertmanager/
- **Blackbox** - https://github.com/prometheus/blackbox_exporter
- **Pushgateway** - https://github.com/prometheus/pushgateway
- **Grafana** - https://grafana.com/
- **Unsee(Decommissioned)** - There has been no commit to this project for a long time (https://github.com/cloudflare/unsee).
- **Elastalert** - This is not covered in this repo (https://github.com/Yelp/elastalert), working on it.

## Note:
- I am using EFS to store all the deployment related files. For example all files for prometheus, blackbox, etc
are stored in EFS and shared by all the k8s clusters.

<p align="center">
  <img width="700" height="370" src="https://files.gitter.im/tomarv2/hhdj/Screen-Shot-2020-04-23-at-8.48.17-AM.png">
</p>

***

There are two options that I use to trigger prometheus repo as part of the CICD process:

- User repo contains a stage `deploy monitoring` which is triggered as part of the project. 

<p align="center">
  <img width="700" height="300" src="https://files.gitter.im/tomarv2/7m11/Screen-Shot-2020-04-11-at-10.04.06-AM.png">
</p>

- Sister repo concept: whenever a project repo is created it creates another repo for project infrastructure which takes care of everything related to infrastructure (like teraform, monitoring, etc).

<p align="center">
  <img width="500" height="475" src="https://files.gitter.im/tomarv2/J3HU/Screen-Shot-2020-04-12-at-6.59.21-PM.png">
</p>

***




