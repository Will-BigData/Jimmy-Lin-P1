from mysql.connector import Error
from connections.ConnectionUtil import ConnectionUtil

class OrderDAO:
    def get_order_by_id(self, id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM orders WHERE id = %s;"
            cursor.execute(sql,(id,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                print("No user found")
                return None
        except Error as e:
            print("An error has occured while fetching the item")
            print(e)
            pass
        finally:
            cursor.close()

    def get_order_by_user(self, user_id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM orders WHERE user_id = %s;"
            cursor.execute(sql,(user_id,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                print("No user found")
                return None
        except Error as e:
            print("An error has occured while fetching the item")
            print(e)
            pass
        finally:
            cursor.close()
    
    def get_order_by_item(self, item_id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM orders WHERE item_id = %s;"
            cursor.execute(sql,(item_id,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                print("No user found")
                return None
        except Error as e:
            print("An error has occured while fetching the item")
            print(e)
            pass
        finally:
            cursor.close()