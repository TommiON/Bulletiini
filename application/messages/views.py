from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime

from application.messages.models import Message
from application.messages.forms import MessageForm

# tulostaa luettelon kaikista viesteistä
@app.route("/messages", methods=["GET"])
def messages_list():
    return render_template("messageList.html", messages = Message.query.all())

# yksittäisen viestin tarkemmat tiedot
@app.route("/messages/<message_id>", methods=["GET"])
def message_details(message_id):
    message = Message.query.get(message_id)
    return render_template("messageDetails.html", message=message)

# poistaa yksittäisen viestin
@app.route("/messages/delete/<message_id>", methods=["POST"])
@login_required
def messages_delete(message_id):
    messageToBeDeleted = Message.query.get(message_id)
    db.session.delete(messageToBeDeleted)
    db.session.commit()
    return redirect(url_for("messages_list"))

# palauttaa lomakkeen viestin editoimiseen (väliaikainen ratkaisu)
@app.route("/messages/edit/<message_id>", methods=["GET"])
@login_required
def messages_editingForm(message_id):
    return render_template("messageEditingForm.html", form=MessageForm(), messageId=message_id)

# korvaa viestin uudella (editointitoiminnallisuus)
@app.route("/messages/edit/<message_id>", methods=["POST"])
@login_required
def messages_edit(message_id):
    message = Message.query.get(message_id)
    form = MessageForm(request.form)
    if not form.validate():
        return render_template("messageEditingForm.html", form=MessageForm(), messageId=message_id)
    message.title = form.title.data
    message.content = form.content.data
    db.session.commit()
    return render_template("messageDetails.html", message=message)