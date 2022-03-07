from flask import Flask

from .extensions import bootstrap, db, migrate
from .security import login_manager
from .views import register_views


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'ChangeMe!'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    register_views(app)

    return app
