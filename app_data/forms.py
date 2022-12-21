from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

# Create a form class that inherits from FlaskForm
# This form will have two fields: a string field and a submit button
# The string field will hold the desired Twitter query

class TwitterForm(FlaskForm):
    
    query = StringField('Query', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')
