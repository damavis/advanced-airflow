#!/usr/bin/env bash
export AIRFLOW_IMAGE_NAME=$(basename `pwd`)/airflow
export AIRFLOW_GID=$(id -u "${USER}")
export AIRFLOW_GID=0

docker build -t "${AIRFLOW_IMAGE_NAME}" .
docker-compose up -d
