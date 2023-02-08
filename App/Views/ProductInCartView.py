
from flask import Blueprint,jsonify,request
from Models.ProductInCartModel import ProductInCartModel

product_in_cart_bp = Blueprint('product_in_cart_bp',__name__)

def success(success_msg,code):
   return jsonify({
         'msg':success_msg,
      }),code

def error(error_msg,code):
   return jsonify({
         'error':error_msg,
      }),code

#ROOT
@product_in_cart_bp.route('/')
def index():
   
   data = ProductInCartModel.read_all()
   return jsonify(data)

#READ_BY_ID
@product_in_cart_bp.route('/<id>', methods =['GET'])
def show_product_in_cart_by_id(id):
   product_in_cart = ProductInCartModel.read_by_id(id)
   if product_in_cart:
      success_msg =  f'Success'
      code = 200
      return success(success_msg,code)
   else:
      error_msg = f"Error - Product in Cart with id {id} was not found!"
      code = 404
      return error(error_msg,code)

#CREATE
@product_in_cart_bp.route('/', methods = ['POST'])
def create_new_product_in_cart():
   data = request.json
   shopping_cart_id = data.get('shopping_cart_id')
   product_id = data.get('product_id')
   quantity = data.get('quantity')

   if (shopping_cart_id == None or product_id == None  or quantity == None ):
      error_msg = f"Error - Invalid request!"
      code = 400
      return error(error_msg,code)
   else:
      product_in_cart = ProductInCartModel(shopping_cart_id=shopping_cart_id, product_id=product_id, quantity=quantity)
      product_in_cart.insert()
      success_msg = f"Success - Product in Cart shopping_cart_id:{shopping_cart_id},product_id:{product_id} quantity:{quantity}  added with ID: {product_in_cart.id}"
      code = 200
      return success(success_msg,code)

#UPDATE
@product_in_cart_bp.route('/<id>', methods =['PUT'])
def update(id):
   product_in_cart = ProductInCartModel.read_by_id(id)
   data = request.json
   new_quantity = data.get('quantity')

   if (new_quantity == None):
      error_msg = f"Error - Invalid request!"
      code = 400
      return error(error_msg,code)
   else:
      if product_in_cart:
         updated_product_in_cart = product_in_cart.update(new_quantity)
         success_msg = f'Success - Product in Cart  with id {id} has quantity {updated_product_in_cart.quantity}'
         code = 200
         return success(success_msg,code)
      else:
         error_msg = f"Error - Product in Cart with id {id} was not found!"
         code = 404
         return error(error_msg,code)


#DELETE
@product_in_cart_bp.route('/<id>', methods =['DELETE'])
def delete(id):
   product_in_cart = ProductInCartModel.read_by_id(id)
   if product_in_cart:
      product_in_cart.delete()
      success_msg = f'Success - Product in Cart with id {id} is now deleted'
      code = 200 
      return success(success_msg,code)
   else:
      error_msg = f"Error - Product in Cart with id {id} was not found!"
      code = 400
      return error(error_msg,code)

