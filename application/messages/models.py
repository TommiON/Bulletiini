from application import db
from sqlalchemy.sql import text, desc

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(5000), nullable=True)
    time_of_sending = db.Column(db.DateTime(timezone=False))
    author_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=True)

    def __init__(self, title, content, time_of_sending, author_id, thread_id):
        self.title = title
        self.content = content
        self.time_of_sending = time_of_sending
        self.author_id = author_id
        self.thread_id = thread_id

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    @staticmethod
    def messages_left_in_thread(thread_id):
        sql_query = text("SELECT COUNT(message.id) FROM message WHERE message.thread_id = :thread").params(thread=thread_id)
        result = db.engine.execute(sql_query)
        for row in result:
            return row[0]
        
    @staticmethod
    def get_latest_messages(number_to_be_displayed):
        return Message.query.order_by(desc(Message.time_of_sending)).limit(number_to_be_displayed).all()

    @staticmethod
    def total_number_of_messages():
        sqlQuery = text("SELECT COUNT(message.id) FROM message")
        result = db.engine.execute(sqlQuery)
        for row in result:
            return row[0]
