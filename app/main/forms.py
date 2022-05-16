from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Technology', 'Technology'),
    ('Science','Science'),('Food','Food'),('Entertainment','Entertainment'),
    ('History','History')],validators=[DataRequired()])
    post = TextAreaField('Your Inspiring words', validators=[DataRequired()])
    submit = SubmitField('Pitch')