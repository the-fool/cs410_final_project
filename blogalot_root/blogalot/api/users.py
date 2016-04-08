from flask import Blueprint
from flask_login import current_user

from ..services import users
from . import route

bp = Blueprint('users', __name__, url_prefix='/users')

@route(bp, '/')
def whoami():
    return current_user._get_current_object()

@route(bp, '/<user_id>')
def show(user_id):
    return users.get_or_404(user_id)
