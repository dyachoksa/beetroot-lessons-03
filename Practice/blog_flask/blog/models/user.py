import datetime as dt

from passlib.hash import pbkdf2_sha256
from sqlalchemy import func
from flask_login import UserMixin

from blog.extensions import db


class User(UserMixin, db.Model):
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

    def hash_password(self, password: str):
        self.password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password: str):
        return pbkdf2_sha256.verify(password, self.password_hash)
