from DAO.UserDAO import UserDAO

class UserService:
    userdao = UserDAO()

    def signup(self, username, email, password):
        user = {'username':username, 'email':email, 'password':password}
        return self.userdao.create_user(user=user)
    
    def login(self, email, password):
        account = self.userdao.get_user_by_email(email=email)
        if not account:
            return None, 404
        if account['password'] == password:
            return account, 200
        return None, 401
    
    def get_user(self, user_id):
        return self.userdao.get_user_by_id(id=user_id)
    
    def updateFunds(self, id, fund):
        return self.userdao.update_funds(self, id, fund)

