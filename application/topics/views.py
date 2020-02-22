from application import app, db, login_required, login_manager
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from sqlalchemy.sql import text
from application.topics.models import Topic
from application.topics.forms import topic_form

# tulostaa luettelon kaikista aiheista
@app.route("/topics", methods=["GET"])
def topics_list():
    return render_template("topic_list.html", topics = Topic.query.all())

# palauttaa lomakkeen uuden aiheen luomiseksi
@app.route("/topics/new", methods=["GET"])
def topic_creation_form():
    return render_template("topic_creation_form.html", form=topic_form())

# luo uuden aiheen
@app.route("/topics", methods=["POST"])
@login_required(role="ADMIN")
def topic_create():
    form = topic_form(request.form)
    name = form.name.data
    
    # validoidaan syöte
    if not form.validate():
        return render_template("topic_creation_form.html", form = form)
    
    # tarkistetaan löytyykö aihe jo tietokannasta, estetään duplikaatti
    sqlQuery = text("SELECT * FROM topic WHERE topic.name = :new_name").params(new_name=name)
    result = db.engine.execute(sqlQuery)
    rows = result.fetchall()
    if len(rows) > 0:
        # notifikaatio?
        return render_template("topic_list.html", topics = Topic.query.all())
    
    # lisätään tietokantaan
    new_topic = Topic(name = form.name.data)
    db.session.add(new_topic)
    db.session.commit()

    # paluu aihelistaan
    return render_template("topic_list.html", topics = Topic.query.all())

# poistaa aiheen
@app.route("/topics/delete/<topic_id>", methods=["GET"])
# @login_required(role="ADMIN")
def topics_delete(topic_id):
    topic_to_be_deleted = Topic.query.get(topic_id)
    db.session.delete(topic_to_be_deleted)
    db.session.commit()
    return render_template("topic_list.html", topics = Topic.query.all())