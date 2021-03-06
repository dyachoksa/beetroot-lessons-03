from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

bootstrap = Bootstrap5()

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
csrf = CSRFProtect()
