from dotenv import load_dotenv

from . import create_app
from .celery import celery # noqa:

load_dotenv()

app = create_app()
app.app_context().push()
