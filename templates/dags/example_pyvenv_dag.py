from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator
from airflow.utils.dates import days_ago
# from python script import functions here

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'a_scenario_2',
    default_args=default_args,
    description='DAG with PythonVirtualenvOperator',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
)

run_code_task = PythonVirtualenvOperator(
    task_id="run_code",
    python_callable=function1,
    requirements=["pandas", "scikit-learn==1.0.2"],
    system_site_packages=False,
    dag=dag
)

create_file_task = PythonVirtualenvOperator(
    task_id="create_file",
    python_callable=function2,
    requirements=["pandas", "scikit-learn==1.0.2"],
    system_site_packages=False,
    dag=dag
)

run_code_task >> create_file_task
