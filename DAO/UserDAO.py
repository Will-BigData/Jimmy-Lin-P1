from mysql.connector import Error
from connections.ConnectionUtil import ConnectionUtil

class UserDAO:
    def get_user_by_id(self, id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM users WHERE id = %s;"
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
    
    def get_all_users(self):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM users;"
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result
            else:
                print("No user found")
                return None
        except Error:
            print("An error has occured while fetching the item")
            pass