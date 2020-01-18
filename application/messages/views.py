from application import app, db
from flask import render_template, request, redirect, url_for
from application.messages.models import Message

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
    return render_template("messages/messageCreationForm.html")

@app.route("/messages", methods=["POST"])
def messages_create():
    newMessage = Message(request.form.get("title"), request.form.get("content"))
    db.session.add(newMessage)
    db.session.commit()
    return redirect(url_for("messages_list"))