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


def get_user():
    """define function"""
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """define method"""
    user = get_user()
    g.user = user

@app.route('/')
def hello():
    """define function"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
