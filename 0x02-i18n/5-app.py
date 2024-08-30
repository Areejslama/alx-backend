#!/usr/bin/env python3
"""this script to define function"""
from flask import Flask, g, request, render_template
from flask_babel import Babel


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """define function"""
    user_id = request.args.get('login_as', None)
    if user_id is None:
        return None
    return users.get(user_id)


@app.before_request
def before_request():
    """define method"""
    g.user = get_user()


@app.route('/')
def hello():
    """define function"""
    return render_template('5-index.html')
