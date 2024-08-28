#!/usr/bin/env python3
"""This script sets up Babel for localization."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale():
    """Function to select the best match for supported languages."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def welcome():
    """Function to render the welcome page."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
