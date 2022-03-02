from .auth import auth
from .pages import pages


def register_views(app):
    app.register_blueprint(pages)
    app.register_blueprint(auth, url_prefix='/auth')
