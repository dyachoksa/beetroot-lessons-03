from blog.extensions import db


post_tags = db.Table(
    'post_tags', db.Model.metadata,
    db.Column('post_id', db.Integer, db.ForeignKey("posts.id", ondelete="CASCADE"), index=True, nullable=False),
    db.Column('tag_id', db.Integer, db.ForeignKey("tags.id", ondelete="CASCADE"), index=True, nullable=False),
    db.PrimaryKeyConstraint("post_id", "tag_id", name="pk_posts_tags"),
)
