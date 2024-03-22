# -*- coding: utf-8 -*-
import time
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(dag_id='1_4_comparison_timedelta',
          start_date=datetime(2024, 1, 1, 0, 15),
          schedule=timedelta(minutes=30),
          max_active_runs=1,
          catchup=True,
          tags=["scheduling_examples"])

task = PythonOperator(task_id="task",
                      dag=dag,
                      python_callable=lambda: time.sleep(3))
