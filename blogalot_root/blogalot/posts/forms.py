
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required

__all__ = ['NewPostForm', 'UpdatePostForm']


class NewPostForm(Form):
    content = TextField('Content', validators=[Required()])


class UpdatePostForm(Form):
    content = TextField('Content', validators=[Required()])
