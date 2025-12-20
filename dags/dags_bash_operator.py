from airflow.sdk import DAG, chain
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", # 파일명과 dag_id가 일치하도록 구성
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
  
  bash_t1 = BashOperator(
    task_id="bash_t1", # 객체명과 task_id가 일치하도록 구성
    bash_command="echo whoami"
  )

  bash_t2 = BashOperator(
    task_id="bash_t2", # 객체명과 task_id가 일치하도록 구성
    bash_command="echo $HOSTNAME"
  )

  bash_t1 >> bash_t2