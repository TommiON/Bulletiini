from application import db
from sqlalchemy.sql import desc, text

from application.messages.models import Message

def getLatestMessages(number_to_be_displayed):
    return Message.query.order_by(desc(Message.time_of_sending)).limit(number_to_be_displayed).all()

def totalNumberOfMessages():
    sqlQuery = text("SELECT COUNT(message.id) FROM message")
    result = db.engine.execute(sqlQuery)
    for row in result:
        return row[0]