# -*- coding: utf-8 -*-
import time
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(dag_id='3_2_dag_to_be_sensed',
          start_date=datetime(2024, 1, 1),
          schedule="00 * * * *",
          max_active_runs=1,
          catchup=True,
          tags=["scheduling_examples"])

task = PythonOperator(task_id="task",
                      dag=dag,
                      python_callable=lambda: time.sleep(3))
