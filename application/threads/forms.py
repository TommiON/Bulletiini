from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, validators
from application.topics.models import Topic

class new_thread_form(FlaskForm):
    title = StringField(label="Otsikko", validators=[validators.InputRequired(), validators.Length(min=1), validators.Length(max=50)])
    content = TextAreaField(label="Viesti", validators=[validators.Length(max=5000)])
    topics = SelectField(
        label='Aihepiirit',
        choices =[(1,1)]
        # choices = [(topic.id, topic.name) for topic in Topic.query.all()]
    )

    class Meta:
        csrf = False