from application import db
from sqlalchemy.sql import text

from application.messages.models import Message

# sellaisten käyttäjien määrä, joilla ainakin yksi viesti
def totalNumberOfPostingUsers():
    sqlQuery = text("SELECT COUNT(DISTINCT message.authorId) FROM message")
    result = db.engine.execute(sqlQuery)
    for row in result:
        return row[0]