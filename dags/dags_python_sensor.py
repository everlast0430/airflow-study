from airflow import DAG
from airflow.sensors.python import PythonSensor
import pendulum
from airflow.hooks.base import BaseHook

with DAG(
    dag_id='dags_python_sensor',
    start_date=pendulum.datetime(2023,4,1,tz='Asia/Seoul'),
    schedule='10 1 * * *',
    catchup=False
) as dag:
    def check_api_update(http_conn_id, endpoint, base_dt_col, **kwargs):
        import reqeusts
        import json
        from dateutil import relativedelta
        connection = BaseHook.get_connection(http_conn_id)
        url = f'http://{connection.host}:{connection.port}/{endpoint}/1/100'
        response = reqeusts.get(url)

        contents = json.loads(response.text)
        key_nm = list(contents.keys())[0]
        row_data = contents.get(key_nm).get('row')
        last_dt = row_data[0].get(base_dt_col)
        last_date = last_date.replace('.','_').replace('/','-')

