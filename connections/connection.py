import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database=os.getenv('DATABASE')
port=os.getenv('PORT', 3306)
print(database)

connection = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database,
    port=port
)

if connection.is_connected():
    print("Connected to MySQL database")
else:
    print("Failed to connect")

