from application import db
from sqlalchemy.sql import text
# from application.topics.models import Topic
from application.associations import Thread_topic

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    time_of_opening = db.Column(db.DateTime(timezone=False))
    author_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    messages = db.relationship('Message', backref='thread', lazy=True)
    topics = db.relationship('Topic', secondary='Thread_topic', back_populates='threads', cascade="all, delete-orphan", lazy=True)
    def __init__(self, title, time_of_opening, author_id, topics):
        self.title = title
        self.time_of_opening = time_of_opening
        self.author_id = author_id
        self.topics = topics

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    @staticmethod
    def totalNumberOfMessages(thread_id):
        #sqlQuery = text("SELECT COUNT(Message.id) FROM Message WHERE Message.threadId = :thread").params(thread=thread_id)
        sqlQuery = text("SELECT COUNT(message.id) FROM message LEFT JOIN thread ON thread.id = message.thread_id WHERE thread.id = :thread").params(thread=thread_id)
        result = db.engine.execute(sqlQuery)
        for row in result:
            return row[0]