from flask import Blueprint, render_template

from . import route

bp = Blueprint('dashboard', __name__)


@route(bp, '/')
def index():
    print("here")
    return render_template('dashboard.html')
