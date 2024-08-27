#!/usr/bin/env python3
"""this script to define babel"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

app.config['BABEL_DEFAULT_LOCALE'] = "en"
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
babel = Babel(app)


class config:
    """define class"""
    LANGUAGES = ["en", "fr"]

    def get_locale():
        return app.config['BABEL_DEFAULT_LOCALE']

    def get_timezone():
        """define method"""
        return app.config['BABEL_DEFAULT_TIMEZONE']

    @app.route('/')
    def greet():
        """define method"""
        return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
