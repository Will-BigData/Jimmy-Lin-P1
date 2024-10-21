import requests

base_url = "http://127.0.0.1:5000/"

def request_handler(url_extension='', data=None, method='GET'):
    # Construct the full URL
    url = f"{base_url}{url_extension}"
    try:
        if method == 'POST':
            response = requests.post(url, json=data)
        if method == 'PUT':
            response = requests.put(url, json=data)
        if method == 'DELETE':
            response = requests.delete(url)
        else:
            response = requests.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None, None

def test_connection():
    return request_handler()