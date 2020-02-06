from flask import render_template
from application import app
from application.messages.helpers import getLatestMessages, totalNumberOfMessages
from application.users.helpers import totalNumberOfPostingUsers

@app.route("/")
def index():
    return render_template("frontpage.html", \
                            latestMessages=getLatestMessages(numberToBeDisplayed=10), \
                            numberOfMessages=totalNumberOfMessages())   