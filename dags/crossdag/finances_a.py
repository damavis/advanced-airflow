# -*- coding: utf-8 -*-
# Copyright 2020 Aneior Studio, SL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Cross-DAG code for DAG B"""
from datetime import timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.utils.dates import days_ago

DAG_NAME = 'finances_a'
DEFAULT_ARGS = {
    'owner': 'Finances',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['finances+airflow@example.com'],
    'retries': 3,
    'retry_delay': timedelta(seconds=10),
    'email_on_failure': False,
    'email_on_retry': False
}

with DAG(dag_id=DAG_NAME,
         default_args=DEFAULT_ARGS,
         dagrun_timeout=timedelta(minutes=10),
         schedule_interval=None,
         tags=["crossdag"]) as dag:

    income_bookkeep = EmptyOperator(task_id='income_bookkeep',
                                    dag=dag)

    validate_income = EmptyOperator(task_id='validate_income',
                                    dag=dag)

    wait_operations_a_calculate_expenses = ExternalTaskSensor(
        task_id='wait_operations_a_calculate_expenses',
        dag=dag,
        external_dag_id='operations_a',
        external_task_id='calculate_expenses',
        check_existence=True)

    outcome_bookkeep = EmptyOperator(task_id='outcome_bookkeep',
                                     dag=dag)


    finances_a_report = EmptyOperator(task_id='finances_a_report',
                                      dag=dag)

    income_bookkeep >> validate_income >> wait_operations_a_calculate_expenses
    wait_operations_a_calculate_expenses >> outcome_bookkeep >> finances_a_report
