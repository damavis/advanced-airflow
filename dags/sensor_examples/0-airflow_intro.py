from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.sensors.time_delta import TimeDeltaSensor


with DAG(dag_id='0-airflow_intro',
         start_date=datetime(2023, 7, 12),
         schedule_interval='00 4 * * *',
         catchup=True,
         max_active_runs=1,
         tags=['sensor_examples']) as dag:

    start_operator = EmptyOperator(task_id='start_operator')

    load_file_1 = BashOperator(task_id='load_file_1', bash_command='sleep 2')
    load_file_2 = BashOperator(task_id='load_file_2', bash_command='sleep 3')

    create_cluster = BashOperator(task_id='create_cluster', bash_command='sleep 8')
    submit_pyspark_job = BashOperator(task_id='submit_pyspark_job', bash_command='sleep 3')
    delete_cluster = BashOperator(task_id='delete_cluster', bash_command='sleep 8')

    do_something_with_data = BashOperator(task_id='do_something_with_data', bash_command='sleep 2')
    do_something_else_with_data = BashOperator(task_id='do_something_else_with_data', bash_command='sleep 3')

    start_operator \
        >> [load_file_1, load_file_2] \
        >> create_cluster \
        >> submit_pyspark_job \
        >> [delete_cluster, do_something_with_data]

    do_something_with_data >> do_something_else_with_data
