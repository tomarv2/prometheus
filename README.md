**Prometheus**

<p align="center">
  <img width="700" height="370" src="https://files.gitter.im/tomarv2/W5zT/Screen-Shot-2020-04-22-at-11.43.39-PM.png">
</p>

***

There are two options on how to configure project. We trigger prometheus repo as part of the CICD process. Whenever a user triggers the project, at the end we have a stage which triggers `configuring monitoring` which takes care of configuring monitoring for the project.

<p align="center">
  <img width="700" height="300" src="https://files.gitter.im/tomarv2/7m11/Screen-Shot-2020-04-11-at-10.04.06-AM.png">
</p>

<p align="center">
  <img width="500" height="425" src="https://files.gitter.im/tomarv2/J3HU/Screen-Shot-2020-04-12-at-6.59.21-PM.png">
</p>

***
This repo contains 6 components that we use in our environment to monitor our k8s infrastructure:

- Prometheus (https://github.com/prometheus/prometheus)
- Alertmanager (https://prometheus.io/docs/alerting/alertmanager/)
- Blackbox (https://github.com/prometheus/blackbox_exporter)
- Pushgateway (https://github.com/prometheus/pushgateway)
- Unsee - Decommissioned (https://github.com/cloudflare/unsee) - There has been no commit to this project for a long time
- Elastalert (There is not covered in this repo: https://github.com/Yelp/elastalert)




