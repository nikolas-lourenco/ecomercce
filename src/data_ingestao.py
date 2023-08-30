
import pandas as pd
import boto3
from pyarrow import parquet as pq
from pyarrow import Table
from datetime import datetime

def load_csv_to_s3():
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Define the CSV path and S3 bucket name
    csv_path = '/path/to/your/csv/file.csv'
    bucket_name = 'your_bucket_name'
    
    # Upload the file to S3
    s3.upload_file(csv_path, bucket_name, f'raw/olist_customers_dataset.csv')

def transform_to_parquet():
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Download the CSV from S3
    s3.download_file('your_bucket_name', 'raw/olist_customers_dataset.csv', '/tmp/olist_customers_dataset.csv')
    
    # Read the CSV into a DataFrame
    df = pd.read_csv('/tmp/olist_customers_dataset.csv')
    
    # Convert the DataFrame to Parquet
    table = Table.from_pandas(df)
    pq.write_table(table, f'/tmp/data_{datetime.now().strftime("%Y%m%d%H%M%S")}.parquet')
    
    # Upload the Parquet file to S3
    s3.upload_file(f'/tmp/data_{datetime.now().strftime("%Y%m%d%H%M%S")}.parquet', 'your_bucket_name', f'processed/data_{datetime.now().strftime("%Y%m%d%H%M%S")}.parquet')

def main():
    # Load CSV to S3
    load_csv_to_s3()
    
    # Transform CSV to Parquet and upload to S3
    transform_to_parquet()

if __name__ == "__main__":
    main()