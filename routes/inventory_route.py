from flask import Blueprint, jsonify
from controller.InventoryController import InventoryController

inventory_routes = Blueprint('inventory_routes', __name__)
inventory_controller = InventoryController()

@inventory_routes.route('/<int:user_id>/', methods=['GET'])
def get_all_items(user_id):
    i = inventory_controller.getInventoryByUser(user_id)
    return jsonify(i),200