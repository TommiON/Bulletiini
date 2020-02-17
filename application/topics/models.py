from application import db
from sqlalchemy.sql import text
from application.models import Base
from application.associations import Thread_topic

class Topic(Base):
    name = db.Column(db.String(50), nullable=False)
    threads = db.relationship("Thread", secondary="Thread_topic", back_populates="topics", lazy=False)
    
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