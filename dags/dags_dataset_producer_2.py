from airflow import Dataset
from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum

with DAG(
    dag_id='dags_dataset_producer_2',
    schedule='0 7 * * *',
    start_date=pendulum.datetime(2022, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_task = BashOperator(
        task_id='bash_task',
        outlets=['dags_dataset_producer_2'],
        bash_command='echo "producer_2 수행 완료"'
    )