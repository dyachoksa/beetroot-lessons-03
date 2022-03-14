from celery import Celery, Task

celery = Celery(
    __name__,
    # broker=app.config['CELERY_BROKER_URL'],
    # backend=app.config['CELERY_RESULT_BACKEND'],
    imports=['blog.tasks'],
)


def init_celery(app):
    celery.conf.update(app.config)

    return celery
