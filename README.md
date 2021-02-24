<p align="center">
    <a href="https://www.apache.org/licenses/LICENSE-2.0" alt="license">
        <img src="https://img.shields.io/github/license/tomarv2/monitoring" /></a>
    <a href="https://github.com/tomarv2/monitoring/tags" alt="GitHub tag">
        <img src="https://img.shields.io/github/v/tag/tomarv2/monitoring" /></a>
    <a href="https://stackoverflow.com/users/6679867/tomarv2" alt="Stack Exchange reputation">
        <img src="https://img.shields.io/stackexchange/stackoverflow/r/6679867"></a>
    <a href="https://discord.gg/XH975bzN" alt="chat on Discord">
        <img src="https://img.shields.io/discord/813961944443912223?logo=discord"></a>
    <a href="https://twitter.com/intent/follow?screen_name=varuntomar2019" alt="follow on Twitter">
        <img src="https://img.shields.io/twitter/follow/varuntomar2019?style=social&logo=twitter"></a>
</p>

# k8s: Monitoring

This repo is used to deploy monitoring for a k8s cluster. There are two parts to monitoring a k8s cluster:
- Monitoring the cluster itself
- Monitoring the application(s) deployed on the cluster
- Also, there is a component to send alerts on elasticsearch results using elastalert

I am using 6 components to monitor the k8s infrastructure:

- **Prometheus** - https://github.com/prometheus/prometheus
- **Alertmanager** - https://prometheus.io/docs/alerting/alertmanager/
- **Blackbox** - https://github.com/prometheus/blackbox_exporter
- **Pushgateway** - https://github.com/prometheus/pushgateway
- **Grafana** - https://grafana.com/
- **Elastalert** - https://github.com/Yelp/elastalert
- **Unsee(Decommissioned)** - There has been no commit to this project for a long time (https://github.com/cloudflare/unsee).


## Note:
- I am using EFS to store all the deployment related files. For example all files for prometheus, alertmanager, blackbox, etc
are stored in EFS and shared by all the k8s clusters (working on moving out of EFS).

<p align="center">
  <img width="600" height="370" src="https://miro.medium.com/max/1400/1*Tp1kUoGHRPmB4wik1kKHkA.png">
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




