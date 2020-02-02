from application import db

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