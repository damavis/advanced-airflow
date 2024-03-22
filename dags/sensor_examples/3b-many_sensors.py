from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.sensors.time_delta import TimeDeltaSensor


with DAG(dag_id='3b-many_sensors',
         start_date=datetime(2023, 7, 1),
         schedule_interval=None,
         tags=['sensor_examples']) as dag:

    for i in range(20):
        success_after_30s = TimeDeltaSensor(
            task_id=f'success_after_30s_{i+1:02d}',
            delta=timedelta(seconds=30),
            poke_interval=5,
            mode='reschedule'
        )






