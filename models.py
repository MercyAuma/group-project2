# from .app import db

# # db = SQLAlchemy(app)

# # Your models.py file should include the definition of classes 
# # which define the models of your database tables.
# #  Such classes inherit from the class db.Model where db is your SQLAlchemy object. 
# #  Further, you may want to define models implementing custom methods, 
# #  like an home-made __repr__ or a json method to format objects or 
# #  export it to json. It could be helpful to define a base model which will lay the ground for all your other models:

# class Test(db.Model):
#     # __tablename__ = 'test'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30))

#     def __init__(self,name):
#         self.name=name

#     def __repr__(self):
#         return '<Test %r>' % (self.name)