from Service.ItemService import ItemService
from flask import request, abort, jsonify

class ItemController:
    items = ItemService()

    def getItemByID(self, item_id):
        if item_id == None:
            abort(400)
        item = self.items.get_item_by_id(item_id)
        if not item:
            abort(404)
        return item

    def getAllItems(self):
        return self.items.get_all_items()
    
    def addItem(self):
        try:
            item = request.json['item']
            cost = request.json['cost']
            item = self.items.add_item({"item":item, "cost":cost})
            if not item:
                return jsonify({"message":"Item Add Failed"}), 400
            return jsonify({"message":"success"}), 200
        except KeyError as e:
            return jsonify({"message":"Please enter all fields"}), 400
        
    def update_item(self, id):
        try:
            item = request.json['item']
            price = request.json['price']
            if int(price) <= 0:
                return jsonify({"message":"Cannot sell for less than 0"}), 400
            result = self.items.update_item(id, {"item":item, "cost":price})
            if result:
                return jsonify({"message":"success"}), 200
            return jsonify({"message":"An Error has occured"}), 500
        except KeyError as e:
            return jsonify({"message":"Missing Values"}), 400
        
    def delete_item(self, id):
        result = self.items.delete_item(id)
        if result:
            return jsonify({"message":"success"}), 200
        return jsonify({"message":"order not found"}), 404