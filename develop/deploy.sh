#!/bin/bash

NAMESPACE=devops

#----------------------------
# alertmanager
AM_CONFIG_NAME=alertmanager-config
AM_FILE_LOCATION=/Users/varun.tomar/Documents/personal_github/prometheus/alertmanager/config/config.yaml
kubectl create configmap $AM_CONFIG_NAME -n $NAMESPACE --from-file=$AM_FILE_LOCATION

#----------------------------
# blackbox
BB_CONFIG_NAME=blackbox-config
BB_FILE_LOCATION=/Users/varun.tomar/Documents/personal_github/prometheus/blackbox/config/config.yaml
kubectl create configmap $BB_CONFIG_NAME -n $NAMESPACE --from-file=$BB_FILE_LOCATION

#----------------------------
# FAQs
kubectl create configmap demo-config --from-literal=zk-server=devzk.demo.com:2181 -n $NAMESPACE
/bin/script-exporter -config.shell="/bin/sh" -web.listen-address=":9172" -web.telemetry-path="/metrics" -config.file=/etc/script-exporter/script-exporter.yml
