from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Post title', validators=[DataRequired(), Length(max=150)])
    slug = StringField('Slug')
    image_url = StringField('Main image url')
    published_at = DateTimeField('Published at')
    short_content = TextAreaField('Short content', validators=[DataRequired(), Length(max=300)])
    content = TextAreaField('Post content', validators=[DataRequired()], render_kw={'rows': 12})
    submit = SubmitField('Save')
