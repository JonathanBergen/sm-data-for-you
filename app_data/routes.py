from flask import (
    Flask,
    url_for,
    render_template,
    redirect
)
from .forms import TwitterForm


app = Flask(
    __name__, 
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static"
    )
app.config['SECRET_KEY'] = 'mysecretkey'
# app.config.from_object('config.Config')


@app.route("/", methods=["GET", "POST"])
def twitter():
    """Standard `contact` form."""
    form = TwitterForm()
    if form.validate_on_submit():
        return redirect(url_for("https://www.google.com/"))
    return render_template(
        "twitter.jinja2",
        form=form,
        template="form-template"
    )

