from flask import Blueprint, jsonify
from controller.OrderController import OrderController

order_routes = Blueprint('order_routes', __name__)
order_controller = OrderController()

@order_routes.route('/user/<int:user_id>/', methods=['GET'])
def get_order_by_user(user_id):
    return order_controller.get_order_by_user(user_id=user_id)
