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
    
    def get_user_by_email(self, email):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM users WHERE email = %s;"
            cursor.execute(sql,(email,))
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

    def create_user(self, user):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s);"
            cursor.execute(sql,(user['username'], user['email'], user['password']))
            conn.commit()
            print("User created successfully.")
            return {**user, 'id':cursor.lastrowid}
        except Error:
            print("An error has occured while fetching the item")
            return None

    def update_user(self, id, user):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s;"
            cursor.execute(sql,(user['username'], user['email'], user['password'], id))
            conn.commit()
            print("User updated successfully.")
        except Error:
            print("An error has occured while fetching the item")
            pass
    
    def update_funds(self, id, fund):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "UPDATE users SET funds = funds + %s WHERE id = %s;"
            cursor.execute(sql,(fund, id))
            conn.commit()
            print("User updated successfully.")
            return True
        except Error:
            print("An error has occured while fetching the item")
            return False

    def delete_user_by_id(self, id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "DELETE FROM users WHERE id = %s;"
            cursor.execute(sql,(id,))
            conn.commit()
            print("User deleted successfully.")
        except Error:
            print("An error has occured while fetching the item")
            pass