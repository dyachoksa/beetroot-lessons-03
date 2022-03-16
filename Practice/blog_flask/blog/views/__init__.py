from .auth import auth
from .pages import pages
from .posts import posts
from .subscriptions import subscriptions


def register_views(app):
    app.register_blueprint(pages)
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(posts, url_prefix='/posts')
    app.register_blueprint(subscriptions, url_prefix='/subscriptions')
