from application import app, db
from flask import render_template, request, redirect, url_for
from application.users.models import User

@app.route("/users")
def users_list():
    return render_template("users/userlist.html", users = User.query.all())

@app.route("/users/new")
def users_creationForm():
    return render_template("users/userCreationForm.html")

@app.route("/users", methods=["POST"])
def users_create():
    newUser = User(request.form.get("name"), request.form.get("password"), True)
    db.session.add(newUser)
    db.session.commit()
    return redirect(url_for("users_list"))