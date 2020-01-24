from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.users.models import User
from application.authentication.forms import LoginForm

@app.route("/authentication/login", methods = ["GET", "POST"])
def authentication_login():
    if request.method == "GET":
        return render_template("authentication/loginForm.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("authentication/loginForm.html", form = form, error = "Käyttäjänimi tai salasana virheellinen!")

    login_user(user)
    return redirect(url_for("index"))    

@app.route("/authentication/logout")
def authentication_logout():
    logout_user()
    return redirect(url_for("index"))