# from datetime import datetime
from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)
    joined = db.Column(db.DateTime(timezone=False))

    def __init__(self, username, password, isAdmin, joined):
        self.username = username
        self.password = password
        self.isAdmin = isAdmin
        self.joined = joined

