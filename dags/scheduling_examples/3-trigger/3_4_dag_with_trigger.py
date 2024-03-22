# -*- coding: utf-8 -*-
import time
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

dag = DAG(dag_id='3_4_dag_with_trigger',
          start_date=datetime(2024, 1, 1),
          schedule="00 * * * *",
          max_active_runs=1,
          catchup=True,
          tags=["scheduling_examples"])

task = PythonOperator(task_id="task",
                      dag=dag,
                      python_callable=lambda: time.sleep(3))

trigger_task = TriggerDagRunOperator(
    task_id='trigger_task',
    trigger_dag_id='3_3_dag_to_be_triggered',
    dag=dag
)

task >> trigger_task
