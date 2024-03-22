# -*- coding: utf-8 -*-
# Copyright 2020 Aneior Studio, SL
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Problem A"""


from datetime import timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago

DAG_NAME = 'problem_a'
DEFAULT_ARGS = {
    'owner': 'Operations+Finance',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['operations+airflow@example.com', 'finance+airflow@example.com'],
    'retries': 3,
    'retry_delay': timedelta(minutes=10),
    'email_on_failure': False,
    'email_on_retry': False
}

with DAG(dag_id=DAG_NAME,
         default_args=DEFAULT_ARGS,
         dagrun_timeout=timedelta(minutes=10),
         schedule_interval=None) as dag:

    calculate_revenue = EmptyOperator(task_id='operations_calculate_revenue',
                                      dag=dag)

    income_bookkeep = EmptyOperator(task_id='finances_income_bookkeep',
                                    dag=dag)

    validate_income = EmptyOperator(task_id='finances_validate_income',
                                    dag=dag)

    calculate_expenses = EmptyOperator(task_id='operations_calculate_expenses',
                                       dag=dag)

    outcome_bookkeep = EmptyOperator(task_id='finances_outcome_bookkeep',
                                     dag=dag)

    operations_a_report = EmptyOperator(task_id='operations_a_report',
                                        dag=dag)

    finance_a_report = EmptyOperator(task_id='finance_a_report',
                                     dag=dag)

    calculate_revenue >> income_bookkeep >> validate_income
    calculate_expenses >> outcome_bookkeep

    validate_income >> finance_a_report
    outcome_bookkeep >> finance_a_report

    income_bookkeep >> operations_a_report
    outcome_bookkeep >> operations_a_report
