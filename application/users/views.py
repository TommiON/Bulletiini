from application import app, db
from flask import render_template, request, redirect, url_for
from application.users.models import User
from application.users.forms import UserCreationForm
from datetime import datetime

@app.route("/users", methods=["GET"])
def users_list():
    return render_template("userList.html", users=User.query.all()) 

@app.route("/users/<user_id>", methods=["GET"])
def user_details(user_id):
    user = User.query.get(user_id)
    return render_template("userDetails.html", user=user)

@app.route("/users/new", methods=["GET"])
def users_creationForm():
    return render_template("userCreationForm.html", form=UserCreationForm())

@app.route("/users", methods=["POST"])
def users_create():
    form = UserCreationForm(request.form)

    if not form.validate():
        return render_template("userCreationForm.html", form = form)

    newUser = User(form.username.data, form.password.data, False, datetime.now())
    db.session.add(newUser)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/users/<user_id>/", methods=["POST"])
def user_change_admin_status(user_id):
    user = User.query.get(user_id)
    user.isAdmin = not user.isAdmin
    
    db.session.commit()

    return redirect(url_for("users_list"))

