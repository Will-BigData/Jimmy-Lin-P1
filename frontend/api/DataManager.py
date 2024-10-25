from .api import *

class DataManager:
    __items = None
    __user = None
    __orders = None
    __inventory = None

    def get_user():
        return DataManager.__user
    
    def signup(username, email, password):
        response = signup(username, email, password)
        if response.status_code == 200:
            return True
        return False

    def login(email, password):
        response = login(email, password)
        if response.status_code == 200:
            DataManager.__user = response.json()
        return response.status_code
    
    def logout():
        DataManager.__user = None
        DataManager.__orders = None
        DataManager.__inventory = None

    def get_items(refetch=False):
        if not DataManager.__items or refetch:
            DataManager.__items = get_items().json()
        return DataManager.__items
    
    def add_item(item):
        response = add_item(item)
        print(response.status_code)
        if response.status_code == 200:
            DataManager.get_items(refetch=True)
            return True
    
    def update_item(id, item):
        response = update_item(id, item)
        if response.status_code == 200:
            DataManager.get_items(refetch=True)
            DataManager.get_orders(refetch=True)
            DataManager.get_inventory(refetch=True)
            return True
        
    def delete_item(id):
        response = delete_item(id)
        print(id)
        print(response.status_code)
        if response.status_code == 200:
            DataManager.get_items(refetch=True)
            DataManager.get_orders(refetch=True)
            DataManager.get_inventory(refetch=True)
            return True

    def update_funds(funds):
        if not DataManager.__user:
            return
        id = DataManager.__user['id']
        response = update_funds(id,funds)
        if response.status_code == 200:
            DataManager.__user['funds']+=funds
        return DataManager.__user['funds']
    
    def get_orders(refetch=False):
        if not DataManager.__user:
            DataManager.__orders = None
            return []
        if not DataManager.__orders or refetch:
            id = DataManager.__user['id']
            DataManager.__orders = get_orders(id).json()
        return DataManager.__orders
    
    def create_order(item_id, amount):
        id = DataManager.__user['id']
        response = create_order(id, item_id, amount)
        if response.status_code == 200:
            DataManager.get_orders(refetch=True)
            return True

    def update_order(order_id, amount):
        response = update_order(order_id, amount)
        if response.status_code == 200:
            DataManager.get_orders(refetch=True)
            return True

    def delete_order(order_id):
        response = delete_order(order_id)
        if response.status_code == 200:
            DataManager.get_orders(refetch=True)
            return True

    def commit_order():
        id = DataManager.__user['id']
        response = commit_order(id)
        if response.status_code == 200:
            DataManager.get_orders(refetch=True)
            DataManager.get_inventory(refetch=True)
            DataManager.__user['funds']-=response.json()['total']
            return True
        
    def get_inventory(refetch=False):
        if not DataManager.__user:
            DataManager.__inventory = None
            return []
        if not DataManager.__inventory or refetch:
            id = DataManager.__user['id']
            DataManager.__inventory = get_inventory(id).json()
        return DataManager.__inventory
    
    def update_inventory(inv_id, amount):
        response = update_inventory(inv_id, amount)
        if response.status_code == 200:
            DataManager.get_inventory(refetch=True)
            return True