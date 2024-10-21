from DAO.OrderDAO import OrderDAO

class OrderService:
    orderdao = OrderDAO()

    def get_order_by_user(self, user_id):
        return self.orderdao.get_order_by_user(user_id=user_id, name=True)
    
    def create_order(self, user_id, item_id, amount):
        order = {"user_id":user_id, "item_id":item_id, "amount":amount}
        return self.orderdao.create_order(order=order)
    
    def update_order(self, id, amount):
        order = {"id":id, "amount":amount}
        return self.orderdao.update_order(id=id,order=order)
    
    def delete_order(self, id):
        return self.orderdao.delete_order(id=id)