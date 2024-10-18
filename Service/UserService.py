from DAO.UserDAO import UserDAO

class UserService:
    userdao = UserDAO()

    def signup(self, username, email, password):
        user = {'username':username, 'email':email, 'password':password}
        return self.userdao.create_user(user=user)
    
    def login(self, email, password):
        account = self.userdao.get_user_by_email(email=email)
        if not account:
            return None
        if account['password'] == password:
            return account
        return None

