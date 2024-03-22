# -*- coding: utf-8 -*-
import time
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.utils.state import State

dag = DAG(dag_id='3_1_dag_with_sensor',
          start_date=datetime(2024, 1, 1),
          schedule="00 * * * *",
          max_active_runs=1,
          catchup=True,
          tags=["scheduling_examples"])

sensor_task = ExternalTaskSensor(
    task_id='sensor_task',
    dag=dag,
    external_dag_id='3_2_dag_to_be_sensed',
    external_task_id=None,
    mode='reschedule',
    poke_interval=10,
    allowed_states=[State.SUCCESS]
)

task = PythonOperator(task_id="task",
                      dag=dag,
                      python_callable=lambda: time.sleep(3))

sensor_task >> task
