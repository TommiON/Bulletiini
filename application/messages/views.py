from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from datetime import datetime

from application.messages.models import Message
from application.messages.forms import MessageForm


@app.route("/messages", methods=["GET"])
def messages_list():
    return render_template("messageList.html", messages = Message.query.all())

@app.route("/messages/<message_id>", methods=["GET"])
def message_details(message_id):
    # miten käsitellään jos id viittaa olemattomaan viestiin?
    message = Message.query.get(message_id)
    return render_template("messageDetails.html", message=message)

@app.route("/messages/new", methods=["GET"])
@login_required
def messages_creationForm():
    return render_template("messageCreationForm.html", form=MessageForm())

@app.route("/messages", methods=["POST"])
@login_required
def messages_create():
    form = MessageForm(request.form)

    if not form.validate():
        return render_template("messageCreationForm.html", form = form)

    newMessage = Message(form.title.data, form.content.data, datetime.now())

    db.session.add(newMessage)
    db.session.commit()
    
    return redirect(url_for("messages_list"))