# -*- coding: utf-8 -*-
import time
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.timetables.interval import DeltaDataIntervalTimetable

dag = DAG(dag_id='2_2_timetable_delta',
          start_date=datetime(2024, 1, 1, 0, 15),
          schedule=DeltaDataIntervalTimetable(timedelta(minutes=30)),
          max_active_runs=1,
          catchup=True,
          tags=["scheduling_examples"])

task = PythonOperator(task_id="task",
                      dag=dag,
                      python_callable=lambda: time.sleep(3))
