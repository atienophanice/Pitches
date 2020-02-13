from . import db

class User (db.Model):
    __tablename__ = 'users'
    id= db.Column(db.String(255))
    