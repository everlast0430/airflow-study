from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.models import Variable
import pendulum, datetime

with DAG(
    dag_id="dags_bash_with_variable",
    schedule="10 9 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz='Asia/Seoul'),
    catchup=False
) as dag:
    val_value = Variable.get("sample_key")

    bash_val_1 = BashOperator(
        task_id="bash_val_1",
        bash_command=f"echo variable:{val_value}"
    )

    bash_val_2 = BashOperator(
        task_id="bash_val_2",
        bash_command=f"echo varible:{{ var.value.sample_key }}"
    )

    bash_val_1 >> bash_val_2
