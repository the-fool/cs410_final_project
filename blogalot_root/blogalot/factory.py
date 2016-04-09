from flask import Flask
from flask_security import SQLAlchemyUserDatastore

from .core import db, security, migrate
from .helpers import register_blueprints
from .middleware import HTTPMethodOverrideMiddleware
from .models import User, Role


def create_app(package_name, package_path,
               settings_override=None,
               register_security_blueprint=True):
    
    app = Flask(package_name, instance_relative_config=True)

    app.config.from_object('blogalot.settings')
    app.config.from_pyfile('settings.cfp', silent=True)
    app.config.from_object(settings_override)

    db.init_app(app)
    migrate.init_app(app, db=db)

    security.init_app(app, datastore=SQLAlchemyUserDatastore(db, User, Role),
                      register_blueprint=register_security_blueprint)

    register_blueprints(app, package_name, package_path)

    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

    return app


