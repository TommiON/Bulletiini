from application import app, db, login_required, login_manager
from flask import render_template, request, redirect, url_for
from flask_login import current_user
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

# poistaa yksittäisen viestin, sallittu vain viestin kirjoittaneelle
@app.route("/messages/delete/<message_id>", methods=["POST"])
@login_required(role="BASIC")
def messages_delete(message_id):
    message_to_be_deleted = Message.query.get(message_id)
    if message_to_be_deleted.author_id != current_user.id:
        return login_manager.unauthorized()
    db.session.delete(message_to_be_deleted)
    db.session.commit()
    return redirect(url_for("index"))

# palauttaa lomakkeen viestin editoimiseen (väliaikainen ratkaisu)
@app.route("/messages/edit/<message_id>", methods=["GET"])
@login_required(role="BASIC")
def messages_editingForm(message_id):
    return render_template("messageEditingForm.html", form=MessageForm(), message_id=message_id)

# korvaa viestin uudella (editointitoiminnallisuus), sallittu vain viestin kirjoittaneelle
@app.route("/messages/edit/<message_id>", methods=["POST"])
@login_required(role="BASIC")
def messages_edit(message_id):
    message = Message.query.get(message_id)
    if message.author_id != current_user.id:
        return login_manager.unauthorized()
    form = MessageForm(request.form)
    if not form.validate():
        return render_template("messageEditingForm.html", form=MessageForm(), message_id=message_id)
    message.title = form.title.data
    message.content = form.content.data
    db.session.commit()
    return render_template("messageDetails.html", message=message)