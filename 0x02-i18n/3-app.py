#!/usr/bin/env python3
"""this script define function"""
from flask import Flask, render_template
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


@app.route('/')
def hello():
    """define function"""
    title = _("home_title")
    header = _("home_header")

    return render_template('3-index.html', title=title, header=header)


if __name__ == '__main__':
    app.run()
