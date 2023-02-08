from dataclasses import dataclass
from . import db

@dataclass
class ProductInCartModel(db.Model):
   __tablename__ = 'product_in_cart'
   id: int
   shopping_cart_id: int 
   product_id: int 
   quantity: int

   id = db.Column(db.Integer, primary_key = True)
   shopping_cart_id = db.Column(db.Integer, db.ForeignKey('shopping_cart.id'))
   product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
   quantity = db.Column(db.Integer)

   def __init__(self, shopping_cart_id, product_id, quantity):
      self.shopping_cart_id = shopping_cart_id
      self.product_id = product_id
      self.quantity = quantity

   def insert(self):
      db.session.add(self)
      db.session.commit()

   @staticmethod
   def read_all():
      data = ProductInCartModel.query.all()  
      return data

   @staticmethod
   def read_by_id(id):
      product_in_cart = ProductInCartModel.query.filter_by(id=id).first()
      return product_in_cart

   
   def update(self,new_quantity):
      self.quantity = new_quantity
      db.session.commit()
      return self
   
   def delete(self):
      db.session.delete(self)
      db.session.commit()
      
