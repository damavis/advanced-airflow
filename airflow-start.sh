#!/usr/bin/env bash
export AIRFLOW_GID=$(id -u "${USER}")
export AIRFLOW_GID=0

docker-compose up -d
