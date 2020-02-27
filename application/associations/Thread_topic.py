from application import db

Thread_topic = db.Table('Thread_topic',     
                        db.Column('thread_id', db.Integer, db.ForeignKey('thread.id', ondelete='CASCADE'), primary_key=True), 
                        db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'), primary_key=True)
)