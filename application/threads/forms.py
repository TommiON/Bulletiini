from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, validators, SelectMultipleField, widgets
from application.topics.models import Topic

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class new_thread_form(FlaskForm):
    title = StringField(label="Otsikko", validators=[validators.InputRequired(), validators.Length(min=1), validators.Length(max=50)])
    content = TextAreaField(label="Viesti", validators=[validators.Length(max=5000)])
    topics = MultiCheckboxField(coerce=int)
    
    class Meta:
        csrf = False