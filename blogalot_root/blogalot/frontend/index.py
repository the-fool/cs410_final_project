from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import current_user

from blogalot.posts.forms import NewPostForm
from blogalot.posts.models import Post
from ..services import posts as PostsService

from blogalot.core import db

from . import route

bp = Blueprint('index', __name__)


@route(bp, '/', methods=['GET', 'POST'])
def index():
    form = NewPostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    elif request.method == "POST":
        print(request.form)
        id = request.form['delete_id']
        to_delete = PostsService.get(id)
        PostsService.delete(to_delete)
        flash("\"{0}\" deleted by author: {1}"
              .format(to_delete.content, to_delete.author.name))
        return redirect(url_for('.index'))
    posts = PostsService.all()

    return render_template('posts.html', posts=posts, new_post_form=form)
