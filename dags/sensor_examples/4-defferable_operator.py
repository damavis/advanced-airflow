from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.sensors.time_delta import TimeDeltaSensorAsync


with DAG(dag_id='4-deferrable_operator',
         start_date=datetime(2023, 7, 1),
         schedule_interval=None,
         tags=['sensor_examples']) as dag:

    for i in range(20):
        success_after_30s = TimeDeltaSensorAsync(
            task_id=f'success_after_30s_{i+1:02d}',
            delta=timedelta(seconds=30),
            poke_interval=5
        )






