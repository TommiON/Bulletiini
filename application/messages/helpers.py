from application import db
from sqlalchemy.sql import desc, text

from application.messages.models import Message

def getLatestMessages(numberToBeDisplayed):
    return Message.query.order_by(desc(Message.timeOfSending)).limit(numberToBeDisplayed).all()

def totalNumberOfMessages():
    sqlQuery = text("SELECT COUNT(Message.id) FROM Message")
    result = db.engine.execute(sqlQuery)
    for row in result:
        return row[0]