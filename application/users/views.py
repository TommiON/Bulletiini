from flask import render_template, request, redirect, url_for
from datetime import datetime

from application import app, db
from application.users.models import User
from application.users.forms import UserCreationForm

@app.route("/users", methods=["GET"])
def users_list():
    return render_template("users/userList.html")

@app.route("/users/<user_id>", methods=["GET"])
def user_details(user_id):
    # miten käsitellään jos id viittaa olemattomaan käyttäjään?
    user = User.query.get(user_id)
    return render_template("users/userDetails.html", user=user)
    # myöhemmin tietokantahaku, joka hakee kyseisen käyttäjän viestin kokonaismäärän?

@app.route("/users/new", methods=["GET"])
def users_creationForm():
    return render_template("users/userCreationForm.html", form=UserCreationForm())

@app.route("/users", methods=["POST"])
def users_create():
    # tässä vaiheessa asetetaan kaikki käyttäjät admineiksi, varsinaisessa toteutuksessa kanta-admin voi muuttaa muiden käyttäjien statusta
    form = UserCreationForm(request.form)

    if not form.validate():
        return render_template("users/userCreationForm.html", form = form)

    newUser = User(form.username.data, form.password.data, False, datetime.now())
    db.session.add(newUser)
    db.session.commit()
    return redirect(url_for("index"))