import datetime as dt

from flask import url_for
from sqlalchemy import func

from blog.extensions import db

from .post_tags import post_tags


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="RESTRICT"), index=True, nullable=False
    )
    title = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, unique=True, nullable=False)
    image_url = db.Column(db.String)
    short_content = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    published_at = db.Column(db.DateTime, index=True)
    created_at = db.Column(
        db.DateTime, nullable=False, default=dt.datetime.utcnow, server_default=func.current_timestamp()
    )
    updated_at = db.Column(db.DateTime, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)

    user = db.relationship("User", back_populates="posts")
    tags = db.relationship("Tag", secondary=post_tags, back_populates="posts")
    comments = db.relationship("Comment", back_populates="post")

    def __str__(self):
        return self.title

    def __repr__(self):
        return "<Post id={} title={} published_at={}>".format(self.id, self.title, self.published_at)

    def get_detail_url(self):
        return url_for('posts.show', slug=self.slug)
