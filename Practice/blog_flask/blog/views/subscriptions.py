from flask import Blueprint, redirect, url_for, flash

from blog.constants import NEWSLETTER_WEEKLY
from blog.extensions import db
from blog.forms import SubscribeForm
from blog.models import Subscription

subscriptions = Blueprint('subscriptions', __name__)


@subscriptions.post("/subscribe")
def subscribe():
    form = SubscribeForm()

    if form.validate_on_submit():
        email = form.email.data

        subscription = Subscription(email=email, is_active=True, newsletter_list=NEWSLETTER_WEEKLY)

        db.session.add(subscription)
        db.session.commit()

        flash("Thank you for subscription", "success")

        return redirect(url_for("pages.index"))

    flash("Something went wrong. We can't subscribe you now. Please try again later.", "warning")

    return redirect(url_for('pages.index'))
