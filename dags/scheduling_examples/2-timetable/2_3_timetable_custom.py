# -*- coding: utf-8 -*-
import time
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from timetables.custom_timetable import TimetableWorkdayWeekend

dag = DAG(dag_id='2_3_timetable_custom',
          start_date=datetime(2024, 1, 1),
          schedule=TimetableWorkdayWeekend(),
          max_active_runs=1,
          catchup=True,
          tags=["scheduling_examples"])

task = PythonOperator(task_id="task",
                      dag=dag,
                      python_callable=lambda: time.sleep(3))
