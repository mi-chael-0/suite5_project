from dataclasses import dataclass
from . import db

@dataclass
class ProductModel(db.Model):
   __tablename__ = 'product'
   id: int
   name: str
   description: str
   quantity: int
   price: int


   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100), nullable = False)
   description = db.Column(db.String(100), nullable = False)
   quantity = db.Column(db.Integer, nullable = False)
   price = db.Column(db.Integer, nullable = False)


   def __init__(self, name, description,quantity,price):
      self.name = name
      self.description = description
      self.quantity = quantity
      self.price = price
      

   def insert(self):
      db.session.add(self)
      db.session.commit()

   @staticmethod
   def read_all():
      data = ProductModel.query.all()  
      return data

   @staticmethod
   def read_by_id(id):
      client = ProductModel.query.filter_by(id=id).first()
      return client

   
   def update(self,new_name, new_description, new_quantity, new_price):
      self.name = new_name
      self.description = new_description
      self.quantity = new_quantity
      self.price = new_price
      db.session.commit()
      return self
   
   def delete(self):
      db.session.delete(self)
      db.session.commit()
      
