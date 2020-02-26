from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(5000), nullable=True)
    time_of_sending = db.Column(db.DateTime(timezone=False))
    author_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)

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
