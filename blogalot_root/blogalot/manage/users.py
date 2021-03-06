from flask.ext.script import Command, prompt


from ..users.models import user_datastore, db
from ..services import users


class CreateUserCommand(Command):

    def run(self):
        email = prompt('Email')
        username = prompt('Username')
        password = prompt('Password')
        credit = prompt('Credit')
        data = dict(email=email,
                    credit=credit,
                    name=username,
                    password=password)
        user_datastore.create_user(**data)
        db.session.commit()
        user = users.first(email=email)
        if user:
            print('\nUser created successfully')
            print('User(id=%s email=%s)' % (user.id, user.email))
            return
        print('\nError creating user:')


class DeleteUserCommand(Command):

    def run(self):
        email = prompt('Email')
        user = users.first(email=email)
        if not user:
            print('Invalid user')
            return
        users.delete(user)
        print('User deleted successfully')


class ListUsersCommand(Command):

    def run(self):
        for u in users.all():
            print('User (id=%s name=%s email=%s)' % (u.id, u.name, u.email))
