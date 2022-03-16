import logging

from flask import render_template
from flask_mail import Message
from sqlalchemy import select

from blog.celery import celery
from blog.constants import NEWSLETTER_WEEKLY
from blog.extensions import db, mail
from blog.models import Subscription, Post

logger = logging.getLogger(__name__)


@celery.task
def send_weekly_newsletter():
    logger.info("Sending weekly newsletter...")

    query = select(Subscription.email)\
        .where(Subscription.is_active.is_(True))\
        .where(Subscription.newsletter_list == NEWSLETTER_WEEKLY)

    emails = list(db.session.execute(query).scalars())

    posts = Post.query.filter(Post.published_at.is_not(None)) \
        .order_by(Post.published_at.desc())\
        .limit(3).all()

    context = {
        "posts": posts
    }

    body = render_template("mails/newsletters/weekly/mail.txt", **context)
    html = render_template("mails/newsletters/weekly/mail.html", **context)

    with mail.connect() as conn:
        for email in emails:
            msg = Message(
                subject='BeetBlog Weekly Newsletter',
                recipients=[email],
                body=body,
                html=html,
            )
            conn.send(msg)
