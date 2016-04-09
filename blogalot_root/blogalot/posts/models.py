from ..core import db
from ..helpers import JsonSerializer


class PostJsonSerializer(JsonSerializer):
    pass


class Post(PostJsonSerializer, db.Model):
    __tablename__ = 'posts'

    pk = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(255))
    author_pk = db.Column(db.BigInteger, db.ForeignKey('users.pk'),
                          nullable=False, index=True)
    author = db.relationship('User', backref='user_posts', foreign_keys=[author_pk])
