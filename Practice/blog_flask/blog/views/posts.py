from flask import Blueprint, render_template, redirect, url_for, flash, Markup
from flask_login import current_user, login_required
from slugify import slugify

from blog.forms import PostForm
from blog.models import Post
from blog.extensions import db

posts = Blueprint('posts', __name__)


@posts.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()

    if form.validate_on_submit():
        slug = form.slug.data
        if not slug:
            slug = slugify(form.title.data)

        post = Post(
            title=form.title.data,
            slug=slug,
            image_url=form.image_url.data,
            published_at=form.published_at.data,
            short_content=form.short_content.data,
            content=form.content.data,
            user=current_user
        )

        db.session.add(post)
        db.session.commit()

        flash(Markup(f"Post <em>{post.title}</em> has been successfully added."), 'success')

        return redirect(url_for('pages.index'))

    return render_template('posts/create.html', form=form)
