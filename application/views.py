from flask import render_template
from application import app
from application.messages.helpers import getLatestMessages, totalNumberOfMessages
from application.users.helpers import totalNumberOfPostingUsers

@app.route("/")
def index():
    return render_template("frontpage.html", \
                            latest_messages=getLatestMessages(number_to_be_displayed=10), \
                            number_of_messages=totalNumberOfMessages())   