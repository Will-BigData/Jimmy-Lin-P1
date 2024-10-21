from flask import Blueprint, jsonify
from controller.OrderController import OrderController

order_routes = Blueprint('order_routes', __name__)
order_controller = OrderController()

@order_routes.route('/user/<int:user_id>/', methods=['GET'])
def get_order_by_user(user_id):
    return order_controller.get_order_by_user(user_id=user_id)

@order_routes.route('/', methods=['POST'])
def create_order():
    return order_controller.create_order()

@order_routes.route('/<int:id>/', methods=['DELETE'])
def delete_order(id):
    return order_controller.delete_order(id)

@order_routes.route('/<int:id>/', methods=['PUT'])
def update_order(id):
    return order_controller.update_order(id)

@order_routes.route('/commit/<int:id>/', methods=['PUT'])
def commit_order(id):
    return order_controller.commit_order(id)