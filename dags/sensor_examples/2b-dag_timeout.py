from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.sensors.time_delta import TimeDeltaSensor


def print_email(*args, **kwargs):
    print('='*30)
    print('Hey, falta el fichero')
    print('='*30)


with DAG(dag_id='2b-dag_timeout',
         start_date=datetime(2023, 7, 1),
         schedule_interval=None,
         tags=['sensor_examples']):

    success_after_30s = TimeDeltaSensor(
        task_id='success_after_30s',
        delta=timedelta(seconds=30),
        poke_interval=5,
        on_failure_callback=print_email,
        timeout=10
    )






