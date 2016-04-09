from ..core import Service
from .models import Post


class PostsService(Service):
    __model__ = Post
