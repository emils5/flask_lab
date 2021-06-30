from app import app
from flask import render_template
from models.shop import orders


@app.route('/orders')
def index():
    return render_template('index.html', title = "Home", orders=orders)

@app.route('/orders/int(<index>)')

def orders(int(index)):
    return render_template('order.html', title = "Order", orders=orders)


# @app.route("/<name>")
# def greet(name):
#     return f"Welcome to my awesome website, {name}!"