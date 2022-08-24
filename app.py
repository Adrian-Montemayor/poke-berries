from flask import Flask, render_template

from settings import settings

app = Flask(__name__)
app.config["FLASK_APP"] = settings.flask_app
app.config["FLASK_ENV"] = settings.flask_env

@app.route('/')
def index():
    return render_template('index.html')