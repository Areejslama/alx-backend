#!/usr/bin/env python3
"""this script to define function"""
from flask import Flask, g, request, render_template 

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(self):
    """define function"""
    user_id = request.args.get('login_as', None)
    if user_id is None:
        return None
    return users.get(user_id)


@app.before_request
def before_request(self):
    """define method"""
    user = request.get_user
    g.user = user


@app.route('/')
def hello():
    """define function"""
    return render_template('5-index.html')

