from application import db
from sqlalchemy.sql import text

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    timeOfOpening= db.Column(db.DateTime(timezone=False))
    authorId = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    messages = db.relationship("Message", backref='thread', lazy=True)

    def __init__(self, title, timeOfOpening, authorId):
        self.title = title
        self.timeOfOpening = timeOfOpening
        self.authorId = authorId

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
        sqlQuery = text("SELECT COUNT(Message.id) FROM Message WHERE Message.threadId = :thread").params(thread=thread_id)
        # sqlQuery = text("   SELECT COUNT(message.id) FROM message \
        #                    LEFT JOIN thread ON thread.id = message.threadId \
        #                    WHERE thread.id = :thread").params(thread=thread_id)
        result = db.engine.execute(sqlQuery)
        for row in result:
            return row[0]