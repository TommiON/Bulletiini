from application import app, db
from flask import render_template, request, redirect, url_for
from application.messages.models import Message
from application.messages.forms import MessageForm
from datetime import datetime

@app.route("/messages", methods=["GET"])
def messages_list():
    return render_template("messages/messageList.html", messages = Message.query.all())

@app.route("/messages/<message_id>", methods=["GET"])
def message_details(message_id):
    # miten käsitellään jos id viittaa olemattomaan viestiin?
    message = Message.query.get(message_id)
    return render_template("messages/messageDetails.html", message=message)
    
@app.route("/messages/new", methods=["GET"])
def messages_creationForm():
    return render_template("messages/messageCreationForm.html", form=MessageForm())

@app.route("/messages", methods=["POST"])
def messages_create():
    form = MessageForm(request.form)

    if not form.validate():
        return render_template("messages/messageCreationForm.html", form = form)

    newMessage = Message(form.title.data, form.content.data, datetime.now())

    db.session.add(newMessage)
    db.session.commit()
    
    return redirect(url_for("messages_list"))