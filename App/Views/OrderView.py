
from flask import Blueprint,jsonify,request
from Models.OrderModel import OrderModel

order_bp = Blueprint('order_bp',__name__)

def success(success_msg,code):
   return jsonify({
         'msg':success_msg,
      }),code

def error(error_msg,code):
   return jsonify({
         'error':error_msg,
      }),code

#ROOT
@order_bp.route('/')
def index():
   
   data = OrderModel.read_all()
   return jsonify(data)

#READ_BY_ID
@order_bp.route('/<id>', methods =['GET'])
def show_order_by_id(id):
   order = OrderModel.read_by_id(id)
   if order:
      success_msg =  f'Success - Order with id {id} is done by client {order.client_id} and has status {order.status} '
      code = 200
      return success(success_msg,code)
   else:
      error_msg = f"Error - Order with id {id} was not found!"
      code = 404
      return error(error_msg,code)

#CREATE
@order_bp.route('/', methods = ['POST'])
def create_new_order():
   data = request.json
   status = data.get('status')
   client_id = data.get('client_id')
   if (client_id == None or status == None):
      error_msg = f"Error - Invalid request!"
      code = 400
      return error(error_msg,code)
   else:
      order = OrderModel(client_id=client_id,status=status)
      order.insert()
      success_msg = f"Success - Order from client {client_id} added with ID: {order.id}"
      code = 200
      return success(success_msg,code)

#UPDATE
@order_bp.route('/<id>', methods =['PUT'])
def update(id):
   order = OrderModel.read_by_id(id)
   data = request.json
   new_status = data.get('status')

   if (new_status == None ):
      error_msg = f"Error - Invalid request!"
      code = 400
      return error(error_msg,code)
   else:
      if order:
         updated_order = order.update(new_status)
         success_msg = f'Success - Order with id {id} is {updated_order.status}'
         code = 200
         return success(success_msg,code)
      else:
         error_msg = f"Error - Order with id {id} was not found!"
         code = 404
         return error(error_msg,code)


#DELETE
@order_bp.route('/<id>', methods =['DELETE'])
def delete(id):
   order = OrderModel.read_by_id(id)
   if order:
      order.delete()
      success_msg = f'Success - Order with id {id} is now deleted'
      code = 200 
      return success(success_msg,code)
   else:
      error_msg = f"Error - Order with id {id} was not found!"
      code = 400
      return error(error_msg,code)

