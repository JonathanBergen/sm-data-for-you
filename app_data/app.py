from flask import (
    Flask,
    url_for,
    render_template,
    redirect
)
from .forms import TwitterForm
from .scripts.scraper import Scraper
import sys

from .extensions import csrf


app = Flask(
    __name__, 
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static"
    )
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['WTF_CSRF_SECRET_KEY'] = 'mysupersecretkey'
csrf.init_app(app)

# Since this app will only have one page, we can just define the route here
@app.route("/", methods=["GET", "POST"])

# The function that will be called when the user visits the page
def twitter():
    form = TwitterForm()

    # If the form is submitted and passes validation, run the search with the given parameters
    if form.validate_on_submit():
        scraper = Scraper(form.query.data, form.start_date.data, form.end_date.data, form.num_tweets.data)
        tweets = scraper.scrape()

        # print the first 10 tweets to the console
        for tweet in tweets[:10]:
            print(tweet, flush=True)
    else:
        print(form.errors)
    return render_template(
        "twitter.jinja2",
        form=form,
        template="form-template"
    )

