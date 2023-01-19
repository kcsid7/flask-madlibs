from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"

debug = DebugToolbarExtension(app)

@app.route("/")
def get_prompts():
    """ Generate the prompt for madlibs """
    prompts = story.prompts
    return render_template("madlib-form.html", prompts=prompts)

@app.route("/story")
def madlib_story():
    """ Show the madlib story """
    madlib = story.generate(request.args)
    return render_template("madlib-story.html", story=madlib)