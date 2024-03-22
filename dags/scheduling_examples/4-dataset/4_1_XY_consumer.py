# -*- coding: utf-8 -*-
import time
from datetime import datetime

from airflow import DAG, Dataset
from airflow.operators.python import PythonOperator

dag = DAG(dag_id='4_1_XY_consumer',
          start_date=datetime(2024, 1, 1),
          schedule=[Dataset('X'), Dataset('Y')],
          max_active_runs=1,
          catchup=True,
          tags=["scheduling_examples"])

task = PythonOperator(task_id="task",
                      dag=dag,
                      python_callable=lambda: time.sleep(3))
