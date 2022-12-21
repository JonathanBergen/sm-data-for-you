from flask import Flask
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length
# from wtforms.fields.html5 import DateField

# Create a form class that inherits from FlaskForm
# This form will have two fields: a string field and a submit button
# The string field will hold the desired Twitter query

class TwitterForm(FlaskForm):
    
    # The basic query field, which is interpreted as plain text in the search
    query = StringField('Query', validators=[DataRequired(), Length(min=1, max=140)])


    # The range of dates to search
    start_date = DateField('Beginning Date', format='%Y-%m-%d')
    end_date = DateField('Ending Date', format='%Y-%m-%d')

    # The number of tweets to return
    num_tweets = IntegerField('Number of Tweets', validators=[DataRequired()])

    # The submit button
    submit = SubmitField('Submit')
