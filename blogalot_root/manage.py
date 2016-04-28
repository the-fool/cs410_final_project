from flask.ext.script import Manager
from flask_migrate import MigrateCommand

from blogalot.api import create_app
from blogalot.manage import CreateUserCommand,\
     DeleteUserCommand, ListUsersCommand,\
     DeletePostCommand, ListPostsCommand

manager = Manager(create_app(register_security_blueprint=True))
manager.add_command('create_user', CreateUserCommand())
manager.add_command('delete_user', DeleteUserCommand())
manager.add_command('list_users', ListUsersCommand())
manager.add_command('db', MigrateCommand)
manager.add_command('list_posts', ListPostsCommand())
manager.add_command('delete_post', DeletePostCommand())


if __name__ == "__main__":
    manager.run()
