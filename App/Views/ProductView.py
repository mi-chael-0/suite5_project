
from flask import Blueprint,jsonify,request
from Models.ProductModel import ProductModel

product_bp = Blueprint('product_bp',__name__)

def success(success_msg,code):
   return jsonify({
         'msg':success_msg,
      }),code

def error(error_msg,code):
   return jsonify({
         'error':error_msg,
      }),code

#ROOT
@product_bp.route('/')
def index():
   
   data = ProductModel.read_all()
   return jsonify(data)

#READ_BY_ID
@product_bp.route('/<id>', methods =['GET'])
def show_product_by_id(id):
   product = ProductModel.read_by_id(id)
   if product:
      success_msg =  f'Success - Product with id {id} is {product.name}'
      code = 200
      return success(success_msg,code)
   else:
      error_msg = f"Error - Product with id {id} was not found!"
      code = 404
      return error(error_msg,code)

#CREATE
@product_bp.route('/', methods = ['POST'])
def create_new_product():
   data = request.json
   name = data.get('name')
   description = data.get('description')
   quantity = data.get('quantity')
   price = data.get('price')


   if (name == None or description == None or quantity == None or price == None):
      error_msg = f"Error - Invalid request!"
      code = 400
      return error(error_msg,code)
   else:
      product = ProductModel(name=name, description=description, quantity=quantity, price=price)
      product.insert()
      success_msg = f"Success - Product {name} added with ID: {product.id}"
      code = 200
      return success(success_msg,code)

#UPDATE
@product_bp.route('/<id>', methods =['PUT'])
def update(id):
   product = ProductModel.read_by_id(id)
   data = request.json
   new_name = data.get('name')
   new_description = data.get('description')
   new_quantity = data.get('quantity')
   new_price = data.get('price')

   if (new_name == None or new_description == None or new_quantity == None or new_price == None):
      error_msg = f"Error - Invalid request!"
      code = 400
      return error(error_msg,code)
   else:
      if product:
         updated_prdoduct = product.update(new_name,new_description,new_quantity,new_price)
         success_msg = f'Success - Product with id {id} is {updated_prdoduct.name}'
         code = 200
         return success(success_msg,code)
      else:
         error_msg = f"Error - Product with id {id} was not found!"
         code = 404
         return error(error_msg,code)


#DELETE
@product_bp.route('/<id>', methods =['DELETE'])
def delete(id):
   product = ProductModel.read_by_id(id)
   if product:
      product.delete()
      success_msg = f'Success - Product with id {id} is now deleted'
      code = 200 
      return success(success_msg,code)
   else:
      error_msg = f"Error - Product with id {id} was not found!"
      code = 400
      return error(error_msg,code)

