from flask_wtf import FlaskForm
from wtforms import StringField, validators

class topic_form(FlaskForm):
    name = StringField(label="Aiheen nimi", validators=[validators.InputRequired(), validators.Length(min=1), validators.Length(max=50)])

    class Meta:
        csrf = False