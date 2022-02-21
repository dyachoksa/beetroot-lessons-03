import datetime as dt

from sqlalchemy import (
    create_engine,
    Table, Column, Integer, String, Text, DateTime,
    ForeignKey, PrimaryKeyConstraint,
    func, select
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///blog.sqlite3", echo=True, future=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String)
    created_at = Column(DateTime, nullable=False, default=dt.datetime.utcnow, server_default=func.current_timestamp())

    profile = relationship("Profile", uselist=False, back_populates="user")
    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<User id={} name={} email={}>".format(self.id, self.name, self.email)


class Profile(Base):
    __tablename__ = "profiles"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, autoincrement=False)
    bio = Column(Text, nullable=False)
    profile_image = Column(String)
    created_at = Column(DateTime, nullable=False, default=dt.datetime.utcnow, server_default=func.current_timestamp())

    user = relationship("User", back_populates="profile")

    def __str__(self):
        return f"{self.user.name}'s profile"

    def __repr__(self):
        return f"<Profile user_id={self.user_id} created_at={self.created_at}>"


post_tags = Table(
    'post_tags', Base.metadata,
    Column('post_id', Integer, ForeignKey("posts.id", ondelete="CASCADE"), index=True, nullable=False),
    Column('tag_id', Integer, ForeignKey("tags.id", ondelete="CASCADE"), index=True, nullable=False),
    PrimaryKeyConstraint("post_id", "tag_id", name="pk_posts_tags"),
)


class Post(Base):
    __tablename__  = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="RESTRICT"), index=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published_at = Column(DateTime, index=True)
    created_at = Column(DateTime, nullable=False, default=dt.datetime.utcnow, server_default=func.current_timestamp())

    user = relationship("User", back_populates="posts")
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")

    def __str__(self):
        return self.title

    def __repr__(self):
        return "<Post id={} title={} published_at={}>".format(self.id, self.title, self.published_at)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=dt.datetime.utcnow, server_default=func.current_timestamp())

    posts = relationship("Post", secondary=post_tags, back_populates="tags")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Tag id={self.id} name={self.name}>"


def main():
    # Base.metadata.create_all(engine)

    with Session() as session:
        # ('Alice Simmons', 'alice.simmons@example.com', NULL)
        # ('Guy Bowman', 'guy.bowman@example.com', 'bullseye')
        # alice = User(name="Alice Simmons", email="alice.simmons@example.com", password=None)
        # guy_bowman = User(name="Guy Bowman", email="guy.bowman@example.com", password="bullseye")
        #
        # session.add(alice)
        # session.add(guy_bowman)
        # session.commit()

        q = select(User).where(User.email == "alice.simmons@example.com")
        row = session.execute(q).first()

        alice = row[0]
        print(repr(alice))


if __name__ == "__main__":
    main()
