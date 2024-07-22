from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'mysql_etl_dag',  # DAG name
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval=timedelta(minutes=5),
    start_date=datetime(2023, 7, 21),
    catchup=False,
)

run_etl = BashOperator(
    task_id='run_etl',
    bash_command='bash /home/ubuntu/wrapper_script.sh ',#give a space after the path
    dag=dag,
)
