from application import db
from application.models import Base

Thread_topic = db.Table("Thread_topic", 
                        Base.metadata,
                        db.Column("thread_id", db.Integer, db.ForeignKey("thread.id")), 
                        db.Column("topic_id", db.Integer, db.ForeignKey("topic.id"))
)