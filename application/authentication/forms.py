from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.Length(min=3), validators.Length(max=50)])
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False