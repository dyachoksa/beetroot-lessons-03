from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CommentForm(FlaskForm):
    message = TextAreaField('Your message', validators=[DataRequired(), Length(min=10, max=600)], render_kw={'rows': 3})
    submit = SubmitField('Add comment')
