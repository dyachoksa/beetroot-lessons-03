import datetime as dt

from sqlalchemy import func

from blog.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(
        db.DateTime, nullable=False, default=dt.datetime.utcnow, server_default=func.current_timestamp()
    )
    updated_at = db.Column(db.DateTime, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)

    profile = db.relationship("Profile", uselist=False, back_populates="user")
    posts = db.relationship("Post", back_populates="user")

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<User id={} name={} email={}>".format(self.id, self.name, self.email)
