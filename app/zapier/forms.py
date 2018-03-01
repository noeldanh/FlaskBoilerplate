from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, Book, Post


class PostForm(FlaskForm):
    emails = StringField('Emails', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    technician = StringField('Technician', validators=[DataRequired()])
    submit = SubmitField('Submit')

    # class Meta:
    #     # This overrides the value from the base form.
    #     csrf = False