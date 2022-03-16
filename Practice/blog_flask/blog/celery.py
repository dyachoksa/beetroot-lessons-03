from celery import Celery
from celery.schedules import crontab

celery = Celery(
    __name__,
    # broker=app.config['CELERY_BROKER_URL'],
    # backend=app.config['CELERY_RESULT_BACKEND'],
    imports=['blog.tasks'],
)


def init_celery(app):
    celery.conf.update(app.config)

    celery.conf.beat_schedule = {
        "weekly-newsletter": {
            "task": "blog.tasks.newsletters.send_weekly_newsletter",
            "schedule": crontab(0, 10, day_of_week=[1]),
            # "schedule": crontab("*/5"),
        }
    }

    return celery
