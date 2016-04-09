
from flask_wtf import Form, TextField, Required

__all__ = ['NewPostForm', 'UpdatePostForm']


class NewPostForm(Form):
    content = TextField('Content', validators=[Required()])
    author = TextField('Author', validators=[Required()])


class UpdatePostForm(Form):
    content = TextField('Content', validators=[Required()])
    author = TextField('Author', validators=[Required()])
