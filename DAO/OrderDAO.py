from mysql.connector import Error
from connections.ConnectionUtil import ConnectionUtil

class OrderDAO:
    def get_order_by_id(self, id, name=False):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            if name:
                sql = "SELECT *, orders.id as id FROM orders JOIN items ON orders.item_id = items.id WHERE id = %s;"
            else:
                sql = "SELECT * FROM orders WHERE id = %s;"
            cursor.execute(sql,(id,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                print("No order found")
                return None
        except Error as e:
            print("An error has occured while fetching the item")
            print(e)
            pass
        finally:
            cursor.close()

    def get_order_by_user(self, user_id, name=False):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            if name:
                sql = "SELECT *, orders.id as id FROM orders JOIN items ON orders.item_id = items.id WHERE user_id = %s;"
            else:
                sql = "SELECT * FROM orders WHERE user_id = %s;"
            cursor.execute(sql,(user_id,))
            result = cursor.fetchall()
            if result:
                return result
            else:
                print("No user found")
                return []
        except Error as e:
            print("An error has occured while fetching the item")
            print(e)
            pass
        finally:
            cursor.close()
    
    def get_order_by_item(self, item_id, name=False):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            if name:
                sql = "SELECT *, orders.id as id FROM orders JOIN items ON orders.item_id = items.id WHERE item_id = %s;"
            else:
                sql = "SELECT * FROM orders WHERE item_id = %s;"
            cursor.execute(sql,(item_id,))
            result = cursor.fetchall()
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
            return True
        except Error:
            print("An error has occured while fetching the item")
            return False
        finally:
            cursor.close()

    def update_order(self, id, order):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "UPDATE orders SET amount = %s WHERE id = %s AND commited = FALSE;"
            cursor.execute(sql,(order['amount'], id))
            conn.commit()
            print("Order updated successfully.")
            return True
        except Error:
            print("An error has occured while fetching the item")
            return False
        finally:
            cursor.close()

    def delete_order(self, id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "DELETE FROM orders WHERE id = %s AND commited = FALSE;"
            cursor.execute(sql,(id,))
            conn.commit()
            print("Order deleted successfully.")
            return True
        except Error:
            print("An error has occured while fetching the item")
            return False
        finally:
            cursor.close()

    def get_order_total(self, user_id, cursor=None):
        c = not cursor
        try:
            if c:
                conn = ConnectionUtil.get_connection()
                cursor = conn.cursor(dictionary=True)
            sql = "select sum(price*amount) as total from orders join items on items.id = orders.item_id WHERE commited = false AND user_id = %s;"
            cursor.execute(sql,(user_id,))
            result = cursor.fetchone()
            if result:
                return result.get('total', 0)
            else:
                return 0
        except Error as e:
            print("An error has occured while fetching the item")
            print(e)
            pass
        finally:
            if c:
                cursor.close()

    def commit_order(self, user_id, cursor=None):
        c = not cursor
        try:
            if c:
                conn = ConnectionUtil.get_connection()
                cursor = conn.cursor(dictionary=True)
            sql = "UPDATE orders SET commited = true WHERE commited = false AND user_id = %s;"
            cursor.execute(sql,(user_id,))
            if c:
                conn.commit()
            return True
        except Error as e:
            print("An error has occured while fetching the item")
            print(e)
            return False
        finally:
            if c:
                cursor.close()