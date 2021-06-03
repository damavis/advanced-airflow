@echo off

for %%a in ("%~dp0\.") do set "DIRNAME=%%~nxa"
set AIRFLOW_IMAGE_NAME=%DIRNAME%/airflow
set AIRFLOW_UID=1000
set AIRFLOW_GID=0

docker build -t %AIRFLOW_IMAGE_NAME% .
docker-compose up -d
