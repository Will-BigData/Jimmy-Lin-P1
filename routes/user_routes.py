from flask import Blueprint, jsonify
from controller.UserController import UserController

user_routes = Blueprint('user_routes', __name__)
user_controller = UserController()

@user_routes.route('/signup/', methods=['POST'])
def signup():
    return user_controller.signup()

@user_routes.route('/login/', methods=['PUT'])
def login():
    return user_controller.login()

@user_routes.route('/funds/<int:user_id>', methods=['PUT'])
def updatefunds(user_id):
    return user_controller.updatefunds(id=user_id)

@user_routes.route('/<int:id>/', methods=['GET'])
def get_user(id):
    return user_controller.get_user(id=id)