import requests

base_url = "http://127.0.0.1:5000/"

def request_handler(url_extension='', data=None, method='GET'):
    # Construct the full URL
    url = f"{base_url}{url_extension}"
    try:
        if method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'PUT':
            response = requests.put(url, json=data)
        elif method == 'DELETE':
            response = requests.delete(url)
        else:
            response = requests.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def test_connection():
    return request_handler()

def login(email, password):
    data = {
        "email":email,
        "password":password
    }
    return request_handler(url_extension='user/login/', data=data, method='PUT')

def signup(username, email, password):
    data = {
        "email":email,
        "password":password,
        'username': username
    }
    return request_handler(url_extension='user/signup/', data=data, method='POST')

def get_items():
    return request_handler(url_extension='/item')

def update_funds(user_id, funds):
    return request_handler(f'/user/funds/{user_id}/', {"funds":funds},method='PUT')

def get_orders(user_id):
    return request_handler(f'/order/user/{user_id}/')

def create_order(user_id, item_id, amount):
    data = {
        "user_id": user_id,
        "item_id": item_id,
        "amount": amount
    }
    return request_handler('/order/', data=data, method='POST')

def update_order(id, amount):
    data = {"amount": amount}
    return request_handler(f'/order/{id}/', data=data, method='PUT')

def delete_order(id):
    return request_handler(f'/order/{id}/', method='DELETE')

def commit_order(user_id):
    return request_handler(f'/order/commit/{user_id}/', method='PUT')

def get_inventory(user_id):
    return request_handler(f'/inventory/{user_id}/', method='GET')

def update_inventory(id, amount):
    return request_handler(f'/inventory/{id}/', data={"amount":amount},method='PUT')

def add_item(item):
    return request_handler(f'/item/', data=item, method='POST')

def update_item(id, item):
    return request_handler(f'/item/{id}/', item, method='PUT')

def delete_item(id):
    return request_handler(f'/item/{id}/', method='DELETE')