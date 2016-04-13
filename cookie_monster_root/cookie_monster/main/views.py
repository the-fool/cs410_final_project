from flask import render_template, url_for, request

from . import main

@main.route('/')
def index():
    print(request.args.get('cookies'))
    return "Okie dokie"
