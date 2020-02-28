from application import app, db
from flask import render_template
from application.users.models import User
from application.messages.models import Message
from application.threads.models import Thread

@app.route("/statistics", methods=["GET"])
def statistics():
    # käyttäjien kokonaismäärä
    number_of_users = User.total_number_of_users()
   
    # viestejä lähettäneiden kokonaismäärä
    number_of_posters = User.total_number_of_posting_users()

    # viestien määrä
    number_of_messages = Message.total_number_of_messages()

    # ketjujen määrä
    number_of_threads = Thread.total_number_of_threads()

    return render_template("statistics.html", 
                            number_of_users = number_of_users,
                            number_of_posters = number_of_posters,
                            number_of_messages = number_of_messages,
                            number_of_threads = number_of_threads)