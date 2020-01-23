from flask import render_template, request, redirect, url_for
from datetime import datetime
from flask_login import login_user, logout_user

from application import app, db
from application.users.models import User
from application.users.forms import LoginForm

@app.route("/users", methods=["GET"])
def users_list():
    return render_template("users/userList.html", users = User.query.all())
    # return "Placeholder..."

@app.route("/users/login", methods = ["GET", "POST"])
def users_login():
    if request.method == "GET":
        return render_template("users/loginForm.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("users/loginForm.html", form = form,
                               error = "Käyttäjänimi tai salasana virheellinen!")


    login_user(user)
    return redirect(url_for("index"))    

@app.route("/users/logout")
def users_logout():
    logout_user()
    return redirect(url_for("index"))

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