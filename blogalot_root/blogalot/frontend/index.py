from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

from .posts.forms import NewPostForm
from .posts.models import Post

from .core import db

from . import route

bp = Blueprint('index', __name__)


@route(bp, '/', methods=['GET', 'POST'])
def index():
    form = NewPostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    posts = Post.all()
    return render_template('posts.html', posts=posts)
