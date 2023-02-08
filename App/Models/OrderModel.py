from dataclasses import dataclass
import datetime
from . import db

@dataclass
class OrderModel(db.Model):
   __tablename__ = 'order'

   TYPES = ['pending','shipped','delivered']

   id: int
   status: str
   client_id: int
   created_at: str
   updated_at: str

   id = db.Column(db.Integer, primary_key = True)
   #status = db.Column(sqlalchemy_utils.types.choice.ChoiceType(TYPES))
   status = db.Column(db.String(100))
   created_at = db.Column(db.DateTime)
   updated_at = db.Column(db.DateTime)
   client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
   products = db.relationship("ProductInOrderModel",backref='order')



   def __init__(self, status ,client_id):
      self.status = status
      self.created_at = datetime.datetime.utcnow()
      self.updated_at = datetime.datetime.utcnow()
      self.client_id = client_id

   def insert(self):
      db.session.add(self)
      db.session.commit()

   @staticmethod
   def read_all():
      data = OrderModel.query.all()  
      return data

   @staticmethod
   def read_by_id(id):
      order = OrderModel.query.filter_by(id=id).first()
      return order

   
   def update(self,new_status):
      self.new_status = new_status
      self.updated_at = datetime.datetime.utcnow
      db.session.commit()
      return self
   
   def delete(self):
      db.session.delete(self)
      db.session.commit()
      
