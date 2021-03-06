from flask_wtf import FlaskForm
from wtforms import EmailField
from wtforms.validators import DataRequired, Email


class SubscribeForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
