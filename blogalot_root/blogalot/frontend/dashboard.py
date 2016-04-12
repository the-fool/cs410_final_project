from flask import Blueprint, render_template

from . import route

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@route(bp, '/')
def index():
    return render_template('dashboard.html')
