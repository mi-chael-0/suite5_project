from dataclasses import dataclass
from . import db

@dataclass
class ClientModel(db.Model):
   __tablename__ = 'client'
   id: int
   name: str
   email: str

   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100), nullable = False)
   email = db.Column(db.String(100))
   orders = db.relationship("OrderModel",backref='client')



   def __init__(self, name, email):
      self.name = name
      self.email = email

   def insert(self):
      db.session.add(self)
      db.session.commit()

   @staticmethod
   def read_all():
      data = ClientModel.query.all()  
      return data

   @staticmethod
   def read_by_id(id):
      client = ClientModel.query.filter_by(id=id).first()
      return client

   
   def update(self,new_name,new_email):
      self.name = new_name
      self.email = new_email
      db.session.commit()
      return self
   
   def delete(self):
      db.session.delete(self)
      db.session.commit()
      
