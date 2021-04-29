FROM apache/airflow:master-python3.8

RUN pip install airflow-pentaho-plugin==1.0.7
