import datetime as dt

from sqlalchemy import func

from blog.extensions import db


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False
    )
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id", ondelete="CASCADE"), index=True, nullable=False)
    message = db.Column(db.String, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=dt.datetime.utcnow, server_default=func.current_timestamp()
    )
    updated_at = db.Column(db.DateTime, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)

    user = db.relationship("User", back_populates="comments")
    post = db.relationship("Post", back_populates="comments")

    def __str__(self):
        return self.message[:20]

    def __repr__(self):
        return f"<Comment id={self.id} post={self.post_id} user={self.user_id}>"
