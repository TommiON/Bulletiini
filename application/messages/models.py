# from datetime import datetime
from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(5000), nullable=True)
    timeOfSending = db.Column(db.DateTime(timezone=False))

    def __init__(self, title, content, timeOfSending):
        self.title = title
        self.content = content
        self.timeOfSending = timeOfSending

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True