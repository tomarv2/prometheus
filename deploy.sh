#!/bin/bash

NAMESPACE=devops

# alertmanager
AM_CONFIG_NAME=alertmanager-config
AM_FILE_LOCATION=/Users/varun.tomar/Documents/personal_github/prometheus/alertmanager/config/config.yaml
kubectl create configmap $AM_CONFIG_NAME -n $NAMESPACE --from-file=$AM_FILE_LOCATION

# blackbox
BB_CONFIG_NAME=blackbox-config
BB_FILE_LOCATION=/Users/varun.tomar/Documents/personal_github/prometheus/blackbox/config/config.yaml
kubectl create configmap $BB_CONFIG_NAME -n $NAMESPACE --from-file=$BB_FILE_LOCATION

# prometheus
RULES_DIR=rules
STATIC_FILES=static-files

for i in "$RULES_DIR"/*
do
  echo "$i"
done

for j in "$STATIC_FILES"/*
do
  echo "$j"
done

# TODO:
kubectl create configmap prometheus-config -n devops --from-file=rules/rules-es-pushgateway.yaml --from-file=rules/rules-infra-monitoring.yaml --from-file=rules/rules-k8s-monitoring.yaml --from-file=rules/rules-redis-exporter.yaml --from-file=rules/rules-spark-blackbox.yaml --from-file=static-files/demo-blackbox.yaml --from-file=static-files/demo1-blackbox.yaml --from-file=static-files/es-pushgateway.yaml --from-file=static-files/infra-monitoring.yaml --from-file=static-files/spark-blackbox.yaml --from-file=config/config.yaml

# Help
# kubectl create configmap demo-config --from-literal=zk-server=devzk.demo.com:2181 -n $NAMESPACE
/bin/script-exporter -config.shell="/bin/sh" -web.listen-address=":9172" -web.telemetry-path="/metrics" -config.file=/etc/script-exporter/script-exporter.yml
kubectl create configmap prometheus-config --from-file=predis_exporter.yaml --from-file=spark-blackbox.yaml --from-file=kubernetes-monitoring.yaml --from-file=config.yaml -n devops

