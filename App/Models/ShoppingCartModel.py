from dataclasses import dataclass
from . import db

@dataclass
class ShoppingCartModel(db.Model):
   __tablename__ = 'shopping_cart'
   id: int
   client_id: int

   id = db.Column(db.Integer, primary_key = True)
   client_id = db.Column(db.Integer, db.ForeignKey('client.id'))


   def __init__(self,client_id):
      self.client_id = client_id

   def insert(self):
      db.session.add(self)
      db.session.commit()

   @staticmethod
   def read_all():
      data = ShoppingCartModel.query.all()  
      return data

   @staticmethod
   def read_by_id(id):
      client = ShoppingCartModel.query.filter_by(id=id).first()
      return client

   
   def update(self,new_name,new_email):
      self.name = new_name
      db.session.commit()
      return self
   
   def delete(self):
      db.session.delete(self)
      db.session.commit()
      
