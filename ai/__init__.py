from . import providers

from .config import configure
from .chat import chat
from .embedding import embedding
from .vision import vision
from .image import image
from .speech import speech
from .moderation import moderation
from .stream import stream


class AI:

    @staticmethod
    def configure(*a, **k):
        return configure(*a, **k)

    @staticmethod
    def chat(*a, **k):
        return chat(*a, **k)

    @staticmethod
    def embedding(*a, **k):
        return embedding(*a, **k)

    @staticmethod
    def vision(*a, **k):
        return vision(*a, **k)

    @staticmethod
    def image(*a, **k):
        return image(*a, **k)

    @staticmethod
    def speech(*a, **k):
        return speech(*a, **k)

    @staticmethod
    def moderation(*a, **k):
        return moderation(*a, **k)

    @staticmethod
    def stream(*a, **k):
        return stream(*a, **k)