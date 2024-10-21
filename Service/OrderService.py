from DAO.OrderDAO import OrderDAO
from DAO.UserDAO import UserDAO
from connections.ConnectionUtil import ConnectionUtil

class OrderService:
    orderdao = OrderDAO()
    userdao = UserDAO()

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
    
    def commit_order(self, id):
        try:
            conn = ConnectionUtil.get_connection()
            cursor = conn.cursor(dictionary=True)
            total = self.orderdao.get_order_total(id, cursor=cursor)
            status = True
            if total == None:
                return 0
            if total > 0:
                status = self.userdao.update_funds(fund=-total, cursor=cursor, id=id)
            if not status:
                return -1
            success = self.orderdao.commit_order(id)
            if not success:
                return -2
            conn.commit()
            return int(total)
        finally:
            cursor.close()