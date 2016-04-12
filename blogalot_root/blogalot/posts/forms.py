
from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import Required

__all__ = ['NewPostForm', 'UpdatePostForm']


class NewPostForm(Form):
    content = TextAreaField('Content', validators=[Required()])


class UpdatePostForm(Form):
    content = TextAreaField('Content', validators=[Required()])
