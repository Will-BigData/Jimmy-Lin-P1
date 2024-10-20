from Service.ItemService import ItemService
from flask import request, abort

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