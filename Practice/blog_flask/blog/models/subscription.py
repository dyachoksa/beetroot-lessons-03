import datetime as dt

from sqlalchemy import func, true, UniqueConstraint

from blog.constants import NEWSLETTER_WEEKLY
from blog.extensions import db


class Subscription(db.Model):
    __tablename__ = "subscriptions"

    __table_args__ = (
        UniqueConstraint('newsletter_list', 'email', name="unq_subscription_email"),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, nullable=False)
    newsletter_list = db.Column(db.String, nullable=False, default=NEWSLETTER_WEEKLY)
    is_active = db.Column(db.Boolean, nullable=False, default=True, server_default=true())
    created_at = db.Column(
        db.DateTime, nullable=False, default=dt.datetime.utcnow, server_default=func.current_timestamp()
    )
    updated_at = db.Column(db.DateTime, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)

    def __str__(self):
        return self.email

    def __repr__(self):
        return f"<Subscription id={self.id} email={self.email} newsletter_list={self.newsletter_list}>"
