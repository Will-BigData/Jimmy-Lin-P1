from Service.InventoryService import InventoryService
from flask import request, abort

class InventoryController:
    inventory = InventoryService()

    def getInventoryByUser(self, user_id):
        return self.inventory.get_inventory_by_user_id(user_id)
