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

    def create_order(self, order):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "INSERT INTO orders (user_id, item_id, amount) VALUES (%s, %s, %s);"
            cursor.execute(sql,(order['user_id'], order['item_id'], order['amount']))
            conn.commit()
            print("Order created successfully.")
        except Error:
            print("An error has occured while fetching the item")
            pass

    def update_order(self, id, order):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "UPDATE orders SET amount = %s WHERE id = %s;"
            cursor.execute(sql,(order['amount'], id))
            conn.commit()
            print("Order updated successfully.")
        except Error:
            print("An error has occured while fetching the item")
            pass

    def delete_order(self, id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "DELETE FROM orders WHERE id = %s;"
            cursor.execute(sql,(id,))
            conn.commit()
            print("Order deleted successfully.")
        except Error:
            print("An error has occured while fetching the item")
            pass