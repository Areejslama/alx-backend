#!/usr/bin/env python3
"""A Basic Flask app"""
from flask_babel import Babel
from flask import Flask, render_template, request


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


@app.route('/')
def welcome():
    """The home"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
