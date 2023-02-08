
from flask import Blueprint,jsonify,request
from Models.ClientModel import ClientModel

client_bp = Blueprint('client_bp',__name__)

def success(success_msg,code):
   return jsonify({
         'msg':success_msg,
      }),code

def error(error_msg,code):
   return jsonify({
         'error':error_msg,
      }),code

#ROOT
@client_bp.route('/')
def index():
   
   data = ClientModel.read_all()
   return jsonify(data)

#READ_BY_ID
@client_bp.route('/<id>', methods =['GET'])
def show_client_by_id(id):
   client = ClientModel.read_by_id(id)
   if client:
      success_msg =  f'Success - Client with id {id} is {client.name} {client.email}'
      code = 200
      return success(success_msg,code)
   else:
      error_msg = f"Error - Client with id {id} was not found!"
      code = 404
      return error(error_msg,code)

#CREATE
@client_bp.route('/', methods = ['POST'])
def create_new_client():
   data = request.json
   name = data.get('name')
   email = data.get('email')
   if (name == None or email == None ):
      error_msg = f"Error - Invalid request!"
      code = 400
      return error(error_msg,code)
   else:
      client = ClientModel(name=name, email=email)
      client.insert()
      success_msg = f"Success - Client {name} {email} added with ID: {client.id}"
      code = 200
      return success(success_msg,code)

#UPDATE
@client_bp.route('/<id>', methods =['PUT'])
def update(id):
   client = ClientModel.read_by_id(id)
   data = request.json
   new_name = data.get('name')
   new_email = data.get('email')

   if (new_name == None or new_email == None ):
      error_msg = f"Error - Invalid request!"
      code = 400
      return error(error_msg,code)
   else:
      if client:
         updated_client = client.update(new_name,new_email)
         success_msg = f'Success - Client with id {id} is {updated_client.name} {updated_client.email}'
         code = 200
         return success(success_msg,code)
      else:
         error_msg = f"Error - Client with id {id} was not found!"
         code = 404
         return error(error_msg,code)


#DELETE
@client_bp.route('/<id>', methods =['DELETE'])
def delete(id):
   client = ClientModel.read_by_id(id)
   if client:
      client.delete()
      success_msg = f'Success - Client with id {id} is now deleted'
      code = 200 
      return success(success_msg,code)
   else:
      error_msg = f"Error - Client with id {id} was not found!"
      code = 400
      return error(error_msg,code)



#READ_CLIENTS_ORDERS_BY_ID
@client_bp.route('/<id>/orders', methods =['GET'])
def show_clients_orders_by_id(id):
   client = ClientModel.read_by_id(id)
   if client:
      return jsonify(client.orders)
   else:
      error_msg = f"Error - Client with id {id} was not found!"
      code = 404
      return error(error_msg,code)