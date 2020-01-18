from application import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(5000), nullable=True)
    # timeOfSending = 
    # lisäksi viitevaimet

    def __init__(self, title, content):
        self.title = title
        self.content = content