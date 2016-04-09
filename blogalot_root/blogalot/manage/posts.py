from flask.ext.script import Command, prompt
from werkzeug.datastructures import MultiDict

class CreatePostCommand(Command):

    def run(self):
        content = prompt("Content")
        user_name = prompt("User name")
        data = MultiDict(dict(content=content, user_name=user_name))
