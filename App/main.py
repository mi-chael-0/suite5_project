from flask import Flask
import Models
import os
from Views.ClientView import client_bp
from Views.ProductView import product_bp
from Views.ProductInCartView import product_in_cart_bp
from Views.ShoppingCartView import shopping_cart_bp
from Views.OrderView import order_bp
from Views.ProductInOrderView import product_in_order_bp

basedir = os.path.abspath(os.path.dirname(__file__))
db = Models.db

def create_app():
   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
   return app

app = create_app()

with app.app_context():
   db.init_app(app)
   db.create_all()
   app.register_blueprint(client_bp,url_prefix='/clients')
   app.register_blueprint(product_bp,url_prefix='/products')
   app.register_blueprint(order_bp,url_prefix='/orders')
   app.register_blueprint(shopping_cart_bp,url_prefix='/shopping_carts')
   app.register_blueprint(product_in_cart_bp,url_prefix='/product_in_cart')
   app.register_blueprint(product_in_order_bp,url_prefix='/product_in_order')

   app.run(debug=True)
