from flask.ext.script import Command, prompt

from ..services import users, posts
from ..posts.models import Post

class CreatePostCommand(Command):

    def run(self):
        content = prompt("Content")
        user_name = prompt("User name")
        user = users.first(name=user_name)
        if not user:
            print("No user with name: {}".format(user_name))
            return
        new_post = Post(content=content, author=user)
        posts.save(new_post)
        
class DeletePostCommand(Command):

    def run(self):
        id = prompt("ID")
        to_delete = posts.get(id)
        if not to_delete:
            print("No post with id: {}".format(id))
            return
        posts.delete(to_delete)


class ListPostsCommand(Command):

    def run(self):
        for p in posts.all():
            print('Post (id={0}, content={1}'.format(p.id, p.content[:15]))
            
