from application import db
from sqlalchemy.sql import text
from application.models import Base

#Thread_topic = db.Table("Thread_topic", 
#                        Base.metadata,
#                        db.Column("thread_id", db.Integer, db.ForeignKey("thread.id")), 
#                        db.Column("topic_id", db.Integer, db.ForeignKey("topic.id"))
#)

class Topic(Base):
    name = db.Column(db.String(50), nullable=False)
    # threads = db.relationship("Thread", secondary=Thread_topic, backref="topic")
    
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