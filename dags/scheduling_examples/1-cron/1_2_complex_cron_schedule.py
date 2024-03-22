# -*- coding: utf-8 -*-
import time
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(dag_id='1_2_complex_cron_schedule',
          start_date=datetime(2024, 1, 1),
          schedule='00-20/5 7 * * 1-5',
          max_active_runs=1,
          catchup=True,
          tags=["scheduling_examples"],
          description="Wake me up")

task = PythonOperator(task_id="task",
                      dag=dag,
                      python_callable=lambda: time.sleep(3))
