from datetime import datetime

from airflow.models import DAG

from operators.file_sensor_async import FileSensorAsync

doc_md = """
To test this DAG, please create the connection fs_tmp_conn. This can be done executing 
`airflow connections add --conn-uri='fs://airflow:airflow@/?path=%2Fopt%2Fairflow%2Ftmp' fs_tmp_conn`.

The task will wait for a file named 'file.txt' to be dropped in the folder `/opt/airflow/tmp` of the triggerer.
"""

with DAG(dag_id='5-implement_trigger',
         start_date=datetime(2023, 7, 1),
         schedule_interval=None,
         tags=['sensor_examples'],
         doc_md=doc_md) as dag:

    for i in range(5):
        check_file = FileSensorAsync(
            task_id=f'check_file_{i}',
            filepath='file.txt',
            fs_conn_id='fs_tmp_conn',
            recursive=False,
            poll_interval=10
        )


