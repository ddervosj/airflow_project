from datetime import timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'docker_dag',
    default_args=default_args,
    description='DAG with DockerOperator',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
)

t1 = DockerOperator(
    task_id='t1',
    image='iris_image:v1.0.1',
    command='python3 iris_script.py',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    retrieve_output=True,
    mounts=[
        Mount(source="xxx", target="/tmp/Output", type="bind")
    ],
    dag=dag
)
