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