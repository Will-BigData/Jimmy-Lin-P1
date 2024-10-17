from mysql.connector import Error
from connections.ConnectionUtil import ConnectionUtil

class ItemDAO:
    def get_item_by_id(self, item_id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM items WHERE id = %s;"
            cursor.execute(sql,(item_id,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                print("No item found")
                return None
        except Error as e:
            print("An error has occured while fetching the item")
            print(e)
            pass
        finally:
            cursor.close()
    
    def get_all_items(self):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM items;"
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result
            else:
                print("No item found")
                return None
        except Error:
            print("An error has occured while fetching the item")
            pass