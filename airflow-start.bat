@echo off

for %%a in ("%~dp0\.") do set "DIRNAME=%%~nxa"
set AIRFLOW_IMAGE_NAME=%DIRNAME%/airflow

docker build -t %AIRFLOW_IMAGE_NAME% .
docker-compose up -d
