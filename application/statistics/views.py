from application import app, db
from flask import render_template, request, redirect, url_for
from sqlalchemy.sql import text
from application.users.helpers import totalNumberOfPostingUsers
from application.messages.helpers import totalNumberOfMessages

@app.route("/statistics", methods=["GET"])
def statistics():
    # käyttäjien kokonaismäärä
    sqlQuery = text("SELECT COUNT(account.id) FROM account")
    result = db.engine.execute(sqlQuery)
    for row in result:
        number_of_users = row[0]

    # viestejä lähettäneiden kokonaismäärä
    number_of_posters = totalNumberOfPostingUsers()

    # viestien määrä
    number_of_messages = totalNumberOfMessages()

    # ketjujen määrä
    sqlQuery = text("SELECT COUNT(thread.id) FROM thread")
    result = db.engine.execute(sqlQuery)
    for row in result:
        number_of_threads = row[0]

    return render_template("statistics.html", 
                            number_of_users = number_of_users,
                            number_of_posters = number_of_posters,
                            number_of_messages = number_of_messages,
                            number_of_threads = number_of_threads)