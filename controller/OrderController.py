from Service.OrderService import OrderService
from flask import request, jsonify

class OrderController:
    orders = OrderService()

    def get_order_by_user(self, user_id):
        return jsonify(self.orders.get_order_by_user(user_id=user_id)), 200
    
    def create_order(self):
        try:
            user_id = request.json['user_id']
            item_id = request.json['item_id']
            amount = request.json.get('amount', 1)
            if int(amount) <= 0:
                return jsonify({"message":"Cannot buy less than 1 of an item"}), 400
            result = self.orders.create_order(user_id, item_id, amount)
            if result:
                return jsonify({"message":"success"}), 200
            return jsonify({"message":"An Error has occured"}), 500
        except KeyError as e:
            return jsonify({"message":"Missing Values"}), 400
        
    def update_order(self, id):
        try:
            amount = request.json['amount']
            if amount <= 0:
                return jsonify({"message":"Cannot buy less than 1 of an item"}), 400
            result = self.orders.update_order(id, amount)
            if result:
                return jsonify({"message":"success"}), 200
            return jsonify({"message":"An Error has occured"}), 500
        except KeyError as e:
            return jsonify({"message":"Missing Values"}), 400
        
    def delete_order(self, id):
        result = self.orders.delete_order(id)
        if result:
            return jsonify({"message":"success"}), 200
        return jsonify({"message":"order not found"}), 404
    
    def commit_order(self, id):
        result = self.orders.commit_order(id)
        if result == -1:
            return jsonify({"message":"insufficent funds"}), 403
        if result == -2:
            return jsonify({"message":"an error has occured"}), 500
        return jsonify({"total":result}), 200