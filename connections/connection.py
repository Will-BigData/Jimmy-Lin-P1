import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database=os.getenv('DATABASE')
port=os.getenv('PORT', 3306)
print(database)

try:
    # Establish the database connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )

    # Check if the connection is successful
    if connection.is_connected():
        print("Connected to MySQL database")
    else:
        print("Failed to connect to MySQL database")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # Close the connection if it was established
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

