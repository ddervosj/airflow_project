from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'a_scenario_3',
    default_args=default_args,
    description='DAG using pre-build venv v2',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
)


main_task = BashOperator(
    task_id="main_task",
    bash_command="source xxx/bin/activate && python xxx/includes/deliveries/DELIVERY_001/test.py print_file_contents && deactivate",
    dag=dag
)


secondary_task = BashOperator(
    task_id="secondary_task",
    bash_command="source xxx/bin/activate && python xxx/includes/deliveries/DELIVERY_001/test.py main && deactivate",
    dag=dag
)

main_task >> secondary_task
