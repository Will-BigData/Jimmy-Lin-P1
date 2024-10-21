from Service.UserService import UserService
from flask import request, jsonify

class UserController:
    users = UserService()

    def signup(self):
        try:
            username = request.json['username']
            email = request.json['email']
            password = request.json['password']
            user = self.users.signup(username=username, email=email, password=password)
            if not user:
                return jsonify({"message":"This username or email is already in use"}), 409
            return jsonify(user), 200
        except KeyError as e:
            return jsonify({"message":"Please enter all fields"}), 400
        
    def login(self):
        try:
            email = request.json['email']
            password = request.json['password']
            user, status = self.users.login(email=email, password=password)
            if status == 404:
                jsonify({"message": "User Not Found"}), status
            if status == 401:
                jsonify({"message": "Incorrect Password"}), status
            return jsonify(user), 200
        except KeyError as e:
            return jsonify({"message":"Please enter all fields"}), 400
    


