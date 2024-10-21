from flask import Flask
from routes.items_route import item_routes
from routes.user_routes import user_routes
from routes.order_routes import order_routes

app = Flask(__name__)

app.register_blueprint(item_routes, url_prefix='/item')
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(order_routes, url_prefix='/order')

@app.route('/')
def hello_world():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)

