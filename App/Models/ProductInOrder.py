from dataclasses import dataclass
from . import db

@dataclass
class ProductInOrderModel(db.Model):
   __tablename__ = 'product_in_order'
   id: int
   order_id: int
   product_id: int 


   id = db.Column(db.Integer, primary_key = True)
   order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
   product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

   def __init__(self, order_id, product_id):
      self.order_id = order_id
      self.product_id = product_id

   def insert(self):
      db.session.add(self)
      db.session.commit()

   @staticmethod
   def read_all():
      data = ProductInOrderModel.query.all()  
      return data

   @staticmethod
   def read_by_id(id):
      product_in_order = ProductInOrderModel.query.filter_by(id=id).first()
      return product_in_order

   
   def delete(self):
      db.session.delete(self)
      db.session.commit()
      
