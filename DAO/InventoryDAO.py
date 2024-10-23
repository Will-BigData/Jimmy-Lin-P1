from mysql.connector import Error
from connections.ConnectionUtil import ConnectionUtil, logging

class InventoryDAO:
    def get_inventory_by_user(self, user_id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT i.id as id, quantity, item FROM inventory i JOIN items ON items.id = i.item_id WHERE user_id = %s AND quantity > 0 ORDER BY id;"
            cursor.execute(sql,(user_id,))
            result = cursor.fetchall()
            logging.info(f"Executed query: {sql}")
            return result if result else []
        except Error as e:
            logging.error(f"Query execution failed: {e}")
            return None
        
    def commit_to_inventory(self, user_id, cursor=None):
        c = not cursor
        try:
            if c:
                conn = ConnectionUtil.get_connection()
                cursor = conn.cursor(dictionary=True)
            sql = ("INSERT INTO Inventory (user_id, item_id, quantity) SELECT o.user_id, o.item_id, SUM(o.amount) AS total_quantity FROM Orders o WHERE o.commited = FALSE AND o.user_id = %s GROUP BY o.user_id, o.item_id ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity);")
            cursor.execute(sql,(user_id,))
            if c:
                conn.commit()
            logging.info(f"Executed query: {sql}")
            return True
        except Error as e:
            logging.error(f"Query execution failed: {e}")
            return False
        
    def update_inventory(self, id, amount):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "UPDATE inventory SET quantity = quantity + %s WHERE id = %s;"
            cursor.execute(sql,(amount, id))
            conn.commit()
            logging.info(f"Executed query: {sql}")
            return True
        except Error as e:
            logging.error(f"Query execution failed: {e}")
            return False
        finally:
            cursor.close()