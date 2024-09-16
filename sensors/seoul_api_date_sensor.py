from airflow.sensors.base import BaseSensorOperator
from airflow.hooks.base import BaseHook

"""
서울시 공공데이터 API 추출시 특정 날짜 컬럼을 조사하여
배치 날짜 기준 전날 데이터가 존재하는지 체크하는 센서
1. 데이터셋에 날짜 컬럼이 존재하고
2. API 사용시 그 날짜 컬럼으로 ORDER BY DESC 되어 가져온다는 가정하에 사용 가능
"""

class SeoulApiDateSensor(BaseSensorOperator):
    template_fields = ('endpoint',)

    def __init__(self, dataset_nm, base_dt_col, day_off=0, **kwargs):
        """
        dataset_nm: 서울시 공공데이터 포털에서 센싱하고자 하는 데이터셋 명
        base_dt_col: 센싱 기준 컬럼 (yyyy.mm.dd... or yyyy/mm/dd... 형태만 가능)
        day_off: 배치일 기준 생성여부를 확인하고자 하는 날짜 차이를 입력 (기본값 : 0)
        """
        super().__init__(**kwargs)
        self.http_conn_id = 'openapi.seoul.go.kr'