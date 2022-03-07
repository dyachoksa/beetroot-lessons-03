from flask import Blueprint, render_template, redirect, url_for, flash, Markup, request
from flask_login import current_user, login_required
from slugify import slugify

from blog.forms import PostForm
from blog.models import Post
from blog.extensions import db

posts = Blueprint('posts', __name__)


@posts.get("/")
def index():
    if current_user.is_authenticated:
        objects = Post.query.order_by(Post.published_at.desc()).all()
    else:
        objects = Post.query.filter(Post.published_at.is_not(None))\
            .order_by(Post.published_at.desc()).all()

    return render_template("posts/index.html", posts=objects)


@posts.get("/search")
def search():
    term = request.args.get('q', None)

    if not term:
        return redirect(url_for('posts.index'))

    objects = Post.query.filter(Post.published_at.is_not(None)) \
        .filter(Post.title.contains(term) | Post.short_content.contains(term) | Post.content.contains(term))\
        .order_by(Post.published_at.desc()).all()

    return render_template("posts/index.html", posts=objects, term=term)


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

        return redirect(url_for('posts.show', slug=post.slug))

    return render_template('posts/create.html', form=form)


@posts.get("/<slug>")
def show(slug):
    obj = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('posts/show.html', slug=slug, post=obj)


@posts.route("/<slug>/edit", methods=['GET', 'POST'])
def edit(slug):
    obj = Post.query.filter_by(slug=slug).first_or_404()

    form = PostForm(obj=obj)

    if form.validate_on_submit():
        form.populate_obj(obj)

        db.session.commit()

        flash(Markup(f"Post <em>{obj.title}</em> has been successfully added."), 'success')

        return redirect(url_for('posts.show', slug=obj.slug))

    return render_template('posts/edit.html', slug=slug, post=obj, form=form)
