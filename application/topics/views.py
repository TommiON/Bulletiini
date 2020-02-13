from application import app, db, login_required, login_manager
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from application.topics.models import Topic
from application.topics.forms import topic_form

# tulostaa luettelon kaikista aiheista
@app.route("/topics", methods=["GET"])
def topics_list():
    return render_template("topicList.html", topics = Topic.query.all())

# palauttaa lomakkeen uuden aiheen luomiseksi
@app.route("/topics/new", methods=["GET"])
def topic_creation_form():
    return render_template("topicCreationForm.html", form=topic_form())

# luo uuden aiheen, tarvitaan tarkistus sille, että ei luoda toistamiseen samaa aihetta!
@app.route("/topics", methods=["POST"])
@login_required(role="ADMIN")
def topic_create():
    form = topic_form(request.form)
    if not form.validate():
        return render_template("topicCreationForm.html", form = form)
    new_topic = Topic(name = form.name.data)
    db.session.add(new_topic)
    db.session.commit()
    return render_template("topicList.html", topics = Topic.query.all())