from flask.ext.script import Manager
from flask_migrate import MigrateCommand

from blogalot.api import create_app
from blogalot.manage import CreateUserCommand,\
     DeleteUserCommand, ListUsersCommand

manager = Manager(create_app(register_security_blueprint=True))
manager.add_command('create_user', CreateUserCommand())
manager.add_command('delete_user', DeleteUserCommand())
manager.add_command('list_users', ListUsersCommand())
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
