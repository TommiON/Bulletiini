from flask import render_template
from application import app
from application.messages.models import Message
from application.users.models import User

@app.route("/")
def index():
    return render_template("frontpage.html", \
                            latest_messages = Message.get_latest_messages(number_to_be_displayed=10),
                            number_of_messages = Message.total_number_of_messages(),
                            number_of_users = User.total_number_of_posting_users())