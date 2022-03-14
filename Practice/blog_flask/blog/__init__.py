import os

from flask import Flask

from .celery import init_celery
from .extensions import bootstrap, db, migrate, mail
from .security import login_manager
from .views import register_views


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'ChangeMe!'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False

    app.config['MAIL_DEFAULT_SENDER'] = 'no-reply@beetblog.local'
    app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
    app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEBUG'] = False

    app.config['broker_url'] = 'redis://127.0.0.1:6379/5'
    app.config['result_backend'] = 'redis://127.0.0.1:6379/6'

    init_celery(app)

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)

    register_views(app)

    return app
