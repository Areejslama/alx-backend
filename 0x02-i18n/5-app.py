#!/usr/bin/env python3
"""A Basic Flask app"""
from flask_babel import Babel
from flask import Flask, render_template, request, g


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Retrieves the locale for a web page"""
    forced_locale = 'fr'
    if 'locale' in request.args:
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config["LANGUAGES"])

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id):
    """define function"""
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """define method"""
    user_id = request.args.get('login_as', 0)
    g.user = get_user(user_id)

@app.route('/')
def hello():
    """define function"""
    return render_template('5-index.html')
