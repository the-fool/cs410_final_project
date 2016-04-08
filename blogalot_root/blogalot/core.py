from flask_sqlalchemy import SQLAlchemy
from flask_security import Security

db = SQLAlchemy()

security = Security()

class BlogalotError(Exception):

    def __init__(self, msg):
        self.msg = msg
