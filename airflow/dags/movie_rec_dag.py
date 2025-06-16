from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'movie_rec_dag',
    default_args=default_args,
    schedule_interval='0 2 * * *',
    catchup=False
)

train = BashOperator(
    task_id='train_model',
    bash_command='spark-submit --master spark://spark-master:7077 spark/train_job.py',
    dag=dag
)

update = BashOperator(
    task_id='update_recommendations',
    bash_command='python /app/scripts/update_recs.py',
    dag=dag
)

train >> update
