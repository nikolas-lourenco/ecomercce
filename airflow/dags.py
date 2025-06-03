
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Import the functions from data_ingestao.py
from src.data_ingestao import load_csv_to_s3, transform_to_parquet

# Define the default_args dictionary
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG
dag = DAG('ecommerce_data_pipeline',
          default_args=default_args,
          description='An E-commerce Data Pipeline',
          schedule_interval=timedelta(days=1),
          start_date=datetime(2023, 1, 1),
          catchup=False)

# PythonOperator tasks
t1 = PythonOperator(
    task_id='load_csv_to_s3',
    python_callable=load_csv_to_s3,
    dag=dag,
)

t2 = PythonOperator(
    task_id='transform_to_parquet',
    python_callable=transform_to_parquet,
    dag=dag,
)

# Task Dependencies
t1 >> t2