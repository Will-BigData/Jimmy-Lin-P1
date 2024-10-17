from connections.connection import connection
from mysql.connector import Error
from connections.ConnectionUtil import ConnectionUtil

class ItemDAO:
    def get_item_by_id(self, item_id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.coursor(dictionary=True)
            sql = "SELECT * FROM items WHERE id = %s;"
            cursor.execute(sql,(item_id,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                print("No item found")
                return None
        except Error:
            print("An error has occured while fetching the item")
            pass
    
    def get_all_items(self):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.coursor(dictionary=True)
            sql = "SELECT * FROM items;"
            cursor.execute(sql)
            result = cursor.fetch()
            if result:
                return result
            else:
                print("No item found")
                return None
        except Error:
            print("An error has occured while fetching the item")
            pass