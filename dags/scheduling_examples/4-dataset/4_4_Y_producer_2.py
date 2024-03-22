# -*- coding: utf-8 -*-
import time
from datetime import datetime

from airflow import DAG, Dataset
from airflow.operators.python import PythonOperator

dag = DAG(dag_id='4_4_Y_producer_2',
          start_date=datetime(2024, 1, 1),
          schedule='00 * * * *',
          max_active_runs=1,
          catchup=True,
          tags=["scheduling_examples"])

task = PythonOperator(task_id="task",
                      dag=dag,
                      python_callable=lambda: time.sleep(5),
                      outlets=[Dataset('Y')])
