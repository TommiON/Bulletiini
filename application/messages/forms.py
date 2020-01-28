from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class MessageForm(FlaskForm):
    title = StringField("Otsikko", [validators.InputRequired(), validators.Length(min=1), validators.Length(max=50)])
    content = TextAreaField("Viesti", [validators.Length(max=5000)])

    class Meta:
        csrf = False