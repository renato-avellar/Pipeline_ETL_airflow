from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.bash import BashOperator
import pandas as pd
import requests
from bs4 import BeautifulSoup


def extract():
  books = []
  for i in range(1,51):
      url = f'http://books.toscrape.com/catalogue/page-{i}.html'
      response = requests.get(url)
      html = BeautifulSoup(response.content, 'html.parser')
      ol = html.find('ol')
      articles = ol.find_all('article', class_='product_pod')
      for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p', class_='price_color').text
        price = float(price[1:])
        avaliability = article.find('p', class_='instock availability').text
        avaliability = avaliability.strip()
        books.append([title, price, star, avaliability])
  return books

def create_csv(ti):
    books_list = ti.xcom_pull(task_ids = 'extract')
    books = pd.DataFrame(books_list, columns=['Title', 'Price', 'Star_Rating', 'Availability'])
    books.to_csv("books.csv")
      
    
with DAG('books', start_date = datetime(2024,3,1),
         schedule_interval = '30 * * * *', catchup = False) as dag:
  
  extract_task = PythonOperator(
    task_id = 'extract',
    python_callable = extract
  ) 
  
  create_table_task = PostgresOperator(
    task_id = 'create_table',
    postgres_conn_id= 'psql',
    sql='''
      CREATE TABLE IF NOT EXISTS books (
            Id INT,
            Title VARCHAR(255),
            Price DECIMAL(10, 2),
            Star_Rating VARCHAR(50),
            Availability VARCHAR(50)
        );
    '''
  )
     
  create_csv_task = PythonOperator(
    task_id = 'create_csv',
    python_callable = create_csv
  ) 
  
  import_csv_task = BashOperator(
    task_id='import_csv_to_postgresql_task',
    bash_command="""
#!/bin/bash

# Parâmetros de conexão com o banco de dados PostgreSQL
DB_USER="onizuka"
DB_PASSWORD="jones666"
DB_NAME="airflow"

# Caminho para o arquivo CSV
CSV_FILE="~/airflow/books.csv"

# Comando para importar dados do CSV para o PostgreSQL
psql -U $DB_USER -d $DB_NAME -c "\copy books FROM '$CSV_FILE' WITH CSV HEADER DELIMITER ',';"
"""
  )
  extract_task >> create_csv_task >> create_table_task >> import_csv_task