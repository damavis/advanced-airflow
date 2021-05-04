#!/usr/bin/env bash
AIRFLOW_IMAGE_NAME=$(basename "$(pwd)")/airflow
AIRFLOW_UID=$(id -u "${USER}")
AIRFLOW_GID=0

export AIRFLOW_IMAGE_NAME
export AIRFLOW_UID
export AIRFLOW_GID

docker build -t "${AIRFLOW_IMAGE_NAME}" .
docker-compose up -d
