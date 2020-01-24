from flask_wtf import FlaskForm
from wtforms import StringField, validators
  
class UserCreationForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.Length(min=3), validators.Length(max=50)])
    password = StringField("Salasana")
  
    class Meta:
        csrf = False