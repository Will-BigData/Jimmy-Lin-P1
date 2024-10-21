from flask import Blueprint, jsonify
from controller.UserController import UserController

user_routes = Blueprint('user_routes', __name__)
user_controller = UserController()

@user_routes.route('/signup', methods=['POST'])
def signup():
    return user_controller.signup()

@user_routes.route('/login', methods=['PUT'])
def login():
    return user_controller.login()