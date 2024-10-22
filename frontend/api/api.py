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
    print(data)
    return request_handler(url_extension='user/login/', data=data, method='PUT')

def get_items():
    return request_handler(url_extension='/item')

def update_funds(user_id, funds):
    print("Called")
    return request_handler(f'/user/funds/{user_id}/', {"funds":funds},method='PUT')