from connections.connection import connection
from mysql.connector import Error

class ItemDAO:
    def get_item_by_id():
        try:
            cursor = connection.cursor(dictionary=True)
        except Error:
            pass