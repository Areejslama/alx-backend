#!/usr/bin/env python3
"""this script define function"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """define class
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
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route('/')
def hello():
    """define function"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
