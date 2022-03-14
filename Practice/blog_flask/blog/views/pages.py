from flask import Blueprint, render_template

from blog.models import Post, Comment

pages = Blueprint("pages", __name__)


@pages.get("/")
def index():
    latest_posts = Post.query.filter(Post.published_at.is_not(None))\
        .order_by(Post.published_at.desc())\
        .limit(3)\
        .all()

    latest_comments = Comment.query.order_by(Comment.created_at.desc()).limit(5).all()

    return render_template(
        "index.html",
        latest_posts=latest_posts,
        latest_comments=latest_comments
    )
