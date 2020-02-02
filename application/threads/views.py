from application import app, db
from flask import render_template, request, redirect, url_for
from datetime import datetime
from flask_login import login_required, current_user

from application.threads.models import Thread
from application.messages.models import Message
from application.messages.forms import MessageForm

# tulostaa listan kaikista keskusteluketjuista
@app.route("/threads", methods=["GET"])
def thread_list():
    return render_template("threadsList.html", threads=Thread.query.all())

# yksittäisen keskusteluketjun tiedot
@app.route("/threads/<thread_id>", methods=["GET"])
def thread_details(thread_id):
    thread = Thread.query.get(thread_id)
    return render_template("threadDetails.html", thread=thread)

# palauttaa lomakkeen uuden ketjun avaamiseksi
@app.route("/threads/new", methods=["GET"])
@login_required
def thread_openingForm():
    return render_template("messageOpeningForm.html", form=MessageForm())

# palauttaa lomakkeen olemassaolevaan ketjuun vastaamiseksi
@app.route("/threads/<thread_id>/new", methods=["GET"])
@login_required
def thread_responseForm(thread_id):
    return render_template("messageResponseForm.html", form=MessageForm(), threadId=thread_id)

# luo uuden keskusteluketjun
@app.route("/threads", methods=["POST"])
@login_required
def thread_create():
    newThread = Thread(title="väliaikainen otsikko", timeOfOpening=datetime.now(), authorId=current_user.id)
    db.session.add(newThread)
    db.session.commit()
    form = MessageForm(request.form)
    if not form.validate():
        return render_template("messageOpeningForm.html", form = form)
    newMessage = Message(title=form.title.data, content=form.content.data, timeOfSending=datetime.now(), authorId=current_user.id, threadId=newThread.id)
    newThread.title = newMessage.title
    db.session.add(newMessage)
    db.session.commit()
    return render_template("threadDetails.html", thread = newThread)

# lisää uuden viestin ketjuun
@app.route("/threads/<thread_id>", methods=["POST"])
@login_required
def thread_respond(thread_id):
    form = MessageForm(request.form)
    if not form.validate():
        return render_template("messageResponseForm.html", form = form)
    newMessage = Message(title=form.title.data, content=form.content.data, timeOfSending=datetime.now(), authorId=current_user.id, threadId=thread_id)
    db.session.add(newMessage)
    db.session.commit()
    return render_template("threadDetails.html", thread=Thread.query.get(thread_id))

# poistaa ketjun