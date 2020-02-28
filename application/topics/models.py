from application import db
from sqlalchemy.sql import text
from application.associations import Thread_topic

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    threads = db.relationship('Thread', secondary='Thread_topic', back_populates='topics', lazy=True, single_parent=True)
    
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

    @staticmethod
    def topic_already_exists(topic_name):
        sql_query = text("SELECT * FROM topic WHERE topic.name = :new_name").params(new_name=topic_name)
        result = db.engine.execute(sql_query)
        rows = result.fetchall()
        if len(rows) > 0:
            return True
        else:
            return False