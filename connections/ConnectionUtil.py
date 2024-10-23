import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  # Log to a file
    filemode='a'  # Append to the file
)

class ConnectionUtil:
    _connection = None
    _host = os.getenv('HOST')
    _user = os.getenv('USER')
    _password = os.getenv('PASSWORD')
    _database=os.getenv('DATABASE')
    _port=os.getenv('PORT', 3306)

    @staticmethod
    def get_connection():
        if ConnectionUtil._connection is None or not ConnectionUtil._connection.is_connected():
            try:
                ConnectionUtil._connection = mysql.connector.connect(
                    host=ConnectionUtil._host,
                    user=ConnectionUtil._user,
                    password=ConnectionUtil._password,
                    database=ConnectionUtil._database,
                    port=ConnectionUtil._port
                )
                logging.info("Connected to the database successfully.")
            except Error as e:
                logging.error(f"Failed to connect to the database: {e}")
        return ConnectionUtil._connection
