from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from application.users.models import User
from application.users.forms import UserCreationForm
from datetime import datetime

# käyttäjälista
@app.route("/users", methods=["GET"])
def users_list():
    return render_template("userList.html", users=User.query.all()) 


# yksittäisen käyttäjän tiedot
@app.route("/users/<user_id>", methods=["GET"])
def user_details(user_id):
    user = User.query.get(user_id)
    return render_template("userDetails.html", user=user)


# lomake uuden käyttäjän luomiseen
@app.route("/users/new", methods=["GET"])
def users_creationForm():
    return render_template("userCreationForm.html", form=UserCreationForm())


# uuden käyttäjän luominen
@app.route("/users", methods=["POST"])
def users_create():
    form = UserCreationForm(request.form)

    if not form.validate():
        return render_template("userCreationForm.html", form = form)

    new_user = User(form.username.data, form.password.data, False, datetime.now())
    db.session.add(new_user)
    db.session.commit()
    return render_template("userList.html", users=User.query.all()) 


# admin-oikeuksien asetus ja poisotto, vaatii admin-oikeudet
@app.route("/users/<user_id>/", methods=["GET"])
@login_required(role="ADMIN")
def user_change_admin_status(user_id):
    user = User.query.get(user_id)
    user.is_admin = not user.is_admin
    
    db.session.commit()

    return redirect(url_for("users_list"))

# käyttäjätunnuksen poisto, vaatii admin-oikeudet
@app.route("/users/delete/<user_id>", methods=["GET"])
@login_required(role="ADMIN")
def users_delete(user_id):
    user_to_be_deleted = User.query.get(user_id)
    db.session.delete(user_to_be_deleted)
    db.session.commit()
    return render_template("userList.html", users=User.query.all()) 

