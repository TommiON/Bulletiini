from application import db
from sqlalchemy.sql import text
from application.messages.models import Message

class User(db.Model):
    __tablename__ = 'account'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    joined = db.Column(db.DateTime, default=db.func.current_timestamp())
    messages = db.relationship('Message', backref='sender', lazy=True)
    threads = db.relationship('Thread', backref='opener', lazy=True)

    def __init__(self, username, password, is_admin, joined):
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.joined = joined

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if self.is_admin:
            return ["ADMIN", "BASIC"]
        else:
            return ["BASIC"]

    @staticmethod
    def total_number_of_messages(user_id):
        sql_query = text("SELECT COUNT(message.id) FROM message LEFT JOIN account ON account.id = message.author_id WHERE account.id = :user").params(user=user_id)
        result = db.engine.execute(sql_query)
        for row in result:
            return row[0]

    @staticmethod
    def total_number_of_users():
        sql_query = text("SELECT COUNT(account.id) FROM account")
        result = db.engine.execute(sql_query)
        for row in result:
            return row[0]

    @staticmethod
    def total_number_of_posting_users():
        sql_query = text("SELECT COUNT(DISTINCT message.author_id) FROM message")
        result = db.engine.execute(sql_query)
        for row in result:
            return row[0]

