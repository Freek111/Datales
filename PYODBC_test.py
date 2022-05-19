import pyodbc
from dotenv import load_dotenv
import os

load_dotenv("ssms.env")

server = os.getenv('SQL_HOST')
database = os.getenv('SQL_DATABASE')
username = os.getenv('SQL_USER')
password = os.getenv('SQL_PASSWORD')

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute('SELECT * FROM TEST.test;')

columns = [metadata[0] for metadata in cursor.description]

print(columns)

for row in cursor.fetchall():
    print(row)
