from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.sensors.time_delta import TimeDeltaSensor


with DAG(dag_id='1-poke_interval',
         start_date=datetime(2023, 7, 1),
         schedule_interval=None,
         tags=['sensor_examples']) as dag:

    success_after_30s = TimeDeltaSensor(
        task_id='success_after_30s',
        delta=timedelta(seconds=30),
        poke_interval=5
    )

    success_after_30s_exponential = TimeDeltaSensor(
        task_id='success_after_30s_exponential',
        delta=timedelta(seconds=30),
        poke_interval=5,
        exponential_backoff=True
    )

    success_after_30s_exponential_max = TimeDeltaSensor(
        task_id='success_after_30s_exponential_max',
        delta=timedelta(seconds=30),
        poke_interval=5,
        exponential_backoff=True,
        max_wait=15
    )







