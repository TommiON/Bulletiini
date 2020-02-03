# from datetime import datetime
from application import db
from sqlalchemy.sql import text

class User(db.Model):
    __tablename__ = "account"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)
    joined = db.Column(db.DateTime, default=db.func.current_timestamp())
    messages = db.relationship("Message", backref='sender', lazy=True)
    threads = db.relationship("Thread", backref='opener', lazy=True)

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

    @staticmethod
    def totalNumberOfMessages(user_id):
        sqlQuery = text("SELECT COUNT(Message.id) FROM Message WHERE Message.authorId = :user").params(user=user_id)
        result = db.engine.execute(sqlQuery)
        for row in result:
            return row[0]
