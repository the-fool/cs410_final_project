from ..core import db
from ..helpers import JsonSerializer


class PostJsonSerializer(JsonSerializer):
    pass


class Post(PostJsonSerializer, db.Model):
    __tablename__ = 'posts'

    pk = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(255))

    author = db.relationship("User", back_populates="posts")
