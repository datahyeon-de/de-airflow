from airflow import DAG
from airflow.operators.email import EmailOperator

import pendulum
import datetime

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    send_email_task = EmailOperator(
        task_id="send_email_task",
        to="reot1004@naver.com",
        subject="Airflow Email Test Notification",
        html_content="Airflow 작업이 완료되었습니다."
    )