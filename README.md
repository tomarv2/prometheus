**k8s configuring monitoring (prometheus, alertmanager, blackbox, grafana) **

<p align="center">
  <img width="700" height="370" src="https://files.gitter.im/tomarv2/W5zT/Screen-Shot-2020-04-22-at-11.43.39-PM.png">
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
This repo contains 6 components that we use in our environment to monitor our k8s infrastructure:

- **Prometheus** - https://github.com/prometheus/prometheus
- **Alertmanager** - https://prometheus.io/docs/alerting/alertmanager/
- **Blackbox** - https://github.com/prometheus/blackbox_exporter
- **Pushgateway** - https://github.com/prometheus/pushgateway
- **Grafana** - https://grafana.com/
- **Unsee(Decommissioned)** - There has been no commit to this project for a long time (https://github.com/cloudflare/unsee).
- **Elastalert** - This is not covered in this repo (https://github.com/Yelp/elastalert), working on it.




