from Service.InventoryService import InventoryService
from flask import request, jsonify

class InventoryController:
    inventory = InventoryService()

    def getInventoryByUser(self, user_id):
        return self.inventory.get_inventory_by_user_id(user_id)
    
    def updateInventory(self, id):
        amount = int(request.json.get('amount', 0))
        result = self.inventory.update_inventory_by_id(id, amount)
        if result:
            return jsonify({"message":"success"}), 200
        return jsonify({'message': "Not enough Item"}), 400
