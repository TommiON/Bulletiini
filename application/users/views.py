from application import app, db
from flask import render_template, request, redirect, url_for
from application.users.models import User
from datetime import datetime

@app.route("/users", methods=["GET"])
def users_list():
    return render_template("users/userList.html", users = User.query.all())

@app.route("/users/<user_id>", methods=["GET"])
def user_details(user_id):
    # miten käsitellään jos id viittaa olemattomaan käyttäjään?
    user = User.query.get(user_id)
    return render_template("users/userDetails.html", user=user)
    # myöhemmin tietokantahaku, joka hakee kyseisen käyttäjän viestin kokonaismäärän?

@app.route("/users/new", methods=["GET"]    )
def users_creationForm():
    return render_template("users/userCreationForm.html")

@app.route("/users", methods=["POST"])
def users_create():
    # tässä vaiheessa asetetaan kaikki käyttäjät admineiksi, varsinaisessa toteutuksessa kanta-admin voi muuttaa muiden käyttäjien statusta
    newUser = User(request.form.get("name"), request.form.get("password"), True, datetime.now())
    db.session.add(newUser)
    db.session.commit()
    return redirect(url_for("users_list"))