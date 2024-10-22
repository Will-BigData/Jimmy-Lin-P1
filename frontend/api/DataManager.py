from .api import *

class DataManager:
    __items = None
    __user = None

    def get_user():
        return DataManager.__user

    def login(email, password):
        response = login(email, password)
        if response.status_code == 200:
            DataManager.__user = response.json()
            return True
        return False
    
    def logout():
        DataManager.__users = None

    def get_items():
        if not DataManager.__items:
            DataManager.__items = get_items().json()
        return DataManager.__items
    
    def update_funds(funds):
        if not DataManager.__user:
            return
        id = DataManager.__user['id']
        response = update_funds(id,funds)
        if response.status_code == 200:
            DataManager.__user['funds']+=funds
        return DataManager.__user['funds']