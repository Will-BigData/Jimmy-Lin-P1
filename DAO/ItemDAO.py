from mysql.connector import Error
from connections.ConnectionUtil import ConnectionUtil, logging

class ItemDAO:
    def get_item_by_id(self, item_id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM items WHERE id = %s;"
            cursor.execute(sql,(item_id,))
            result = cursor.fetchone()
            logging.info(f"Executed query: {sql}")
            if result:
                return result
            else:
                return None
        except Error as e:
            logging.error(f"Query execution failed: {e}")
        finally:
            cursor.close()
    
    def get_all_items(self):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM items;"
            cursor.execute(sql)
            result = cursor.fetchall()
            logging.info(f"Executed query: {sql}")
            if result:
                return result
            else:
                print("No item found")
                return None
        except Error as e:
            logging.error(f"Query execution failed: {e}")
            pass
    
    def add_items(self, item):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "INSERT INTO items (item, cost) VALUES (%s, %s);"
            cursor.execute(sql)
            conn.commit()
            logging.info(f"Executed query: {sql}")
            return True
        except Error as e:
            logging.error(f"Query execution failed: {e}")
            return False
        finally:
            cursor.close()

    def update_item(self, id, item):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "UPDATE items SET price = %s, item = %s WHERE id = %s;"
            cursor.execute(sql,(item['cost'], item['item'], id))
            conn.commit()
            logging.info(f"Executed query: {sql}")
            return True
        except Error as e:
            logging.error(f"Query execution failed: {e}")
            return False
        finally:
            cursor.close()

    def delete_item(self, id):
        try:
            print(id)
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor()
            sql = "DELETE FROM items WHERE id = %s;"
            cursor.execute(sql,(id,))
            conn.commit()
            logging.info(f"Executed query: {sql}")
            return True
        except Error as e:
            logging.error(f"Query execution failed: {e}")
            return False
        finally:
            cursor.close()