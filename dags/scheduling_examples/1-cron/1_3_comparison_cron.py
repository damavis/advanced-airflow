# -*- coding: utf-8 -*-
import time
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(dag_id='1_3_comparison_cron',
          start_date=datetime(2024, 1, 1, 0, 15),
          schedule="*/30 * * * *",
          max_active_runs=1,
          catchup=False,
          tags=["scheduling_examples"])

task = PythonOperator(task_id="task",
                      dag=dag,
                      python_callable=lambda: time.sleep(3))
