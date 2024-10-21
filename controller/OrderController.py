from Service.OrderService import OrderService
from flask import request, jsonify

class OrderController:
    orders = OrderService()

    def get_order_by_user(self, user_id):
        return jsonify(self.orders.get_order_by_user(user_id=user_id)), 200