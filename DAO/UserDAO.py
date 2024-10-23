from mysql.connector import Error
from connections.ConnectionUtil import ConnectionUtil, logging

class UserDAO:
    def get_user_by_id(self, id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM users WHERE id = %s;"
            cursor.execute(sql,(id,))
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
    
    def get_user_by_email(self, email):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM users WHERE email = %s;"
            cursor.execute(sql,(email,))
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
    
    def get_all_users(self):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM users;"
            cursor.execute(sql)
            result = cursor.fetchall()
            logging.info(f"Executed query: {sql}")
            if result:
                return result
            else:
                return None
        except Error as e:
            logging.error(f"Query execution failed: {e}")

    def create_user(self, user):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s);"
            cursor.execute(sql,(user['username'], user['email'], user['password']))
            conn.commit()
            logging.info(f"Executed query: {sql}")
            return {**user, 'id':cursor.lastrowid}
        except Error as e:
            logging.error(f"Query execution failed: {e}")
            return None

    def update_user(self, id, user):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s;"
            cursor.execute(sql,(user['username'], user['email'], user['password'], id))
            conn.commit()
            logging.info(f"Executed query: {sql}")
        except Error as e:
            logging.error(f"Query execution failed: {e}")
    
    def update_funds(self, id, fund, cursor=None):
        c = not cursor
        try:
            if c:
                conn = ConnectionUtil.get_connection()
                cursor = conn.cursor(dictionary=True)
            sql = "UPDATE users SET funds = funds + %s WHERE id = %s;"
            cursor.execute(sql,(fund, id))
            if c:
                conn.commit()
            logging.info(f"Executed query: {sql}")
            return True
        except Error as e:
            logging.error(f"Query execution failed: {e}")
            return False
        finally:
            if c:
                cursor.close()

    def delete_user_by_id(self, id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "DELETE FROM users WHERE id = %s;"
            cursor.execute(sql,(id,))
            conn.commit()
            logging.info(f"Executed query: {sql}")
        except Error as e:
            logging.error(f"Query execution failed: {e}")