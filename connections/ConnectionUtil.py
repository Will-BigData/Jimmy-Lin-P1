import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

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
                print(f"Connection to MYSQL ${ConnectionUtil._database} Successful")
            except Error as e:
                print(f"Error while connecting to MySQL: {e}")
        return ConnectionUtil._connection
