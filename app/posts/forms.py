from wsgiref.validate import validator

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(message="Обов'язкове поле"), Length(min=3, max=100)])
    content = TextAreaField("Content")
    submit = SubmitField("Submit")


