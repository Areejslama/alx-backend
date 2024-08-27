#!/usr/bin/env python3
"""this script to setup flask"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    """define flask app"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
