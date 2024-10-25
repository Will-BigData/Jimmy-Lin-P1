from flask import Blueprint, jsonify
from controller.ItemController import ItemController

item_routes = Blueprint('item_routes', __name__)
item_controller = ItemController()

@item_routes.route('', methods=['GET'])
def get_all_items():
    i = item_controller.getAllItems()
    return jsonify(i),200

@item_routes.route('/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    i = item_controller.getItemByID(item_id)
    return jsonify(i),200

@item_routes.route('', methods=['POST'])
def add_item():
    return item_controller.addItem()

@item_routes.route('/<int:item_id>/', methods=['PUT'])
def update_item(id):
    return item_controller.update_item(id)

@item_routes.route('/<int:item_id>/', methods=['DELETE'])
def delete_item(id):
    return item_controller.delete_item(id)