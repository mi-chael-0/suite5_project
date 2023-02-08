
from flask import Blueprint,jsonify,request
from Models.ProductInOrder import ProductInOrderModel

product_in_order_bp = Blueprint('product_in_order_bp',__name__)

def success(success_msg,code):
   return jsonify({
         'msg':success_msg,
      }),code

def error(error_msg,code):
   return jsonify({
         'error':error_msg,
      }),code

#ROOT
@product_in_order_bp.route('/')
def index():
   
   data = ProductInOrderModel.read_all()
   return jsonify(data)

#READ_BY_ID
@product_in_order_bp.route('/<id>', methods =['GET'])
def show_product_in_cart_by_id(id):
   product_in_cart = ProductInOrderModel.read_by_id(id)
   if product_in_cart:
      success_msg =  f'Success - Product in Cart has the' # with id {id} is {client.name} {client.email}'
      code = 200
      return success(success_msg,code)
   else:
      error_msg = f"Error - Product in Cart with id {id} was not found!"
      code = 404
      return error(error_msg,code)

#CREATE
@product_in_order_bp.route('/', methods = ['POST'])
def create_new_product_in_order():
   data = request.json
   order_id = data.get('order_id')
   product_id = data.get('product_id')

   if (order_id == None or product_id == None):
      error_msg = f"Error - Invalid request!"
      code = 400
      return error(error_msg,code)
   else:
      product_in_order = ProductInOrderModel(order_id=order_id, product_id=product_id)
      product_in_order.insert()
      success_msg = f"Success - Product in Order order_id:{order_id},product_id:{product_id} added with ID: {product_in_order.id}"
      code = 200
      return success(success_msg,code)



#DELETE
@product_in_order_bp.route('/<id>', methods =['DELETE'])
def delete(id):
   product_in_order = ProductInOrderModel.read_by_id(id)
   if product_in_order:
      product_in_order.delete()
      success_msg = f'Success - Product in Order with id {id} is now deleted'
      code = 200 
      return success(success_msg,code)
   else:
      error_msg = f"Error - Product in Order with id {id} was not found!"
      code = 400
      return error(error_msg,code)

