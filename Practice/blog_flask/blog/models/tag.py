import datetime as dt

from sqlalchemy import func

from blog.extensions import db

from .post_tags import post_tags


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime, nullable=False, default=dt.datetime.utcnow, server_default=func.current_timestamp()
    )
    updated_at = db.Column(db.DateTime, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)

    posts = db.relationship("Post", secondary=post_tags, back_populates="tags")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Tag id={self.id} name={self.name} slug={self.slug}>"
