from application import db
from sqlalchemy.sql import text
# from application.threads.models import Thread
from application.associations import Thread_topic

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    threads = db.relationship('Thread', secondary='Thread_topic', back_populates='topics', lazy=True, cascade='all, delete-orphan', single_parent=True)
    
    def __init__(self, name):
        self.name = name
       
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True