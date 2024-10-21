from DAO.OrderDAO import OrderDAO

class OrderService:
    orderdao = OrderDAO()

    def get_order_by_user(self, user_id):
        return self.orderdao.get_order_by_user(user_id=user_id, name=True)