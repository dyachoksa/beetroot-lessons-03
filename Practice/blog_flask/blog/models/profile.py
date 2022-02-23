import datetime as dt

from sqlalchemy import func

from blog.extensions import db


class Profile(db.Model):
    __tablename__ = "profiles"

    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, autoincrement=False
    )
    bio = db.Column(db.Text, nullable=False)
    profile_image = db.Column(db.String)
    created_at = db.Column(
        db.DateTime, nullable=False, default=dt.datetime.utcnow, server_default=func.current_timestamp()
    )
    updated_at = db.Column(db.DateTime, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)

    user = db.relationship("User", back_populates="profile")

    def __str__(self):
        return f"{self.user.name}'s profile"

    def __repr__(self):
        return f"<Profile user_id={self.user_id} created_at={self.created_at}>"
