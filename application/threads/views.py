from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from datetime import datetime
from flask_login import current_user

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
@login_required(role="BASIC")
def thread_openingForm():
    return render_template("messageOpeningForm.html", form=MessageForm())

# palauttaa lomakkeen olemassaolevaan ketjuun vastaamiseksi
@app.route("/threads/<thread_id>/new", methods=["GET"])
@login_required(role="BASIC")
def thread_responseForm(thread_id):
    return render_template("messageResponseForm.html", form=MessageForm(), thread_id=thread_id)

# luo uuden keskusteluketjun
@app.route("/threads", methods=["POST"])
@login_required(role="BASIC")
def thread_create():
    new_thread = Thread(title="väliaikainen otsikko", time_of_opening=datetime.now(), author_id=current_user.id)
    db.session.add(new_thread)
    db.session.commit()
    form = MessageForm(request.form)
    if not form.validate():
        return render_template("messageOpeningForm.html", form = form)
    new_message = Message(title=form.title.data, content=form.content.data, time_of_sending=datetime.now(), author_id=current_user.id, thread_id=new_thread.id)
    new_thread.title = new_message.title
    db.session.add(new_message)
    db.session.commit()
    return render_template("threadDetails.html", thread = new_thread)

# lisää uuden viestin ketjuun
@app.route("/threads/<thread_id>", methods=["POST"])
@login_required(role="BASIC")
def thread_respond(thread_id):
    form = MessageForm(request.form)
    if not form.validate():
        return render_template("messageResponseForm.html", form = form)
    new_message = Message(title=form.title.data, content=form.content.data, time_of_sending=datetime.now(), author_id=current_user.id, thread_id=thread_id)
    db.session.add(new_message)
    db.session.commit()
    return render_template("threadDetails.html", thread=Thread.query.get(thread_id))

# poistaa ketjun