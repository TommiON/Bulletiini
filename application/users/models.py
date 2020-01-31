# from datetime import datetime
from application import db

class User(db.Model):
    __tablename__ = "account"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)
    joined = db.Column(db.DateTime, default=db.func.current_timestamp())
    messages = db.relationship("Message", backref='sender', lazy=True)

    def __init__(self, username, password, isAdmin, joined):
        self.username = username
        self.password = password
        self.isAdmin = isAdmin
        self.joined = joined

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

