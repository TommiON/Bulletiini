from flask import Flask
app = Flask(__name__)

# tietokannan konfigurointi
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bulletins.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# sovelluksen perusrakenne
from application import views
from application.authentication import views
from application.users import models, views
from application.messages import models, views
from application.threads import models, views

# login-toiminnallisuus
from application.users.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "authentication_login"
login_manager.login_message = "Toiminto vaatii kirjautumisen."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try: 
    db.create_all()
except:
    pass
