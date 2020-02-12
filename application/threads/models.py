from application import db
from sqlalchemy.sql import text
from application.models import Base

Thread_topic = db.Table('Thread_topic', 
                        Base.metadata,
                        db.Column('thread_id', db.Integer, db.ForeignKey('thread.id')), 
                        db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'))
)

class Thread(Base):
    title = db.Column(db.String(50), nullable=False)
    time_of_opening = db.Column(db.DateTime(timezone=False))
    author_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    messages = db.relationship("Message", backref='thread', lazy=True)
    topics = db.relationship("Topic", secondary=Thread_topic, backref='x')

    def __init__(self, title, time_of_opening, author_id):
        self.title = title
        self.time_of_opening = time_of_opening
        self.author_id = author_id

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
    
    class Topic(Base):
        topicLabel = db.Column(db.String(50), nullable=False)
        threads = db.relationship("Thread", secondary=Thread_topic, backref="y")

        def __init__(self, topicLabel):
            self.topicLabel = topicLabel
       
        def get_id(self):
            return self.id

        def is_active(self):
            return True

        def is_anonymous(self):
            return False

        def is_authenticated(self):
            return True