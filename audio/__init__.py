from .convert import convert
from .merge import merge
from .split import split
from .trim import trim
from .volume import increase, decrease
from .effects import fade_in, fade_out, normalize
from .edit import reverse, speed
from .info import duration, channels, sample_rate, metadata


class Audio:

    @staticmethod
    def convert(*a, **k):
        return convert(*a, **k)

    @staticmethod
    def merge(*a, **k):
        return merge(*a, **k)

    @staticmethod
    def split(*a, **k):
        return split(*a, **k)

    @staticmethod
    def trim(*a, **k):
        return trim(*a, **k)

    @staticmethod
    def increase(*a, **k):
        return increase(*a, **k)

    @staticmethod
    def decrease(*a, **k):
        return decrease(*a, **k)
    
    @staticmethod
    def fade_in(*a, **k):
        return fade_in(*a, **k)

    @staticmethod
    def fade_out(*a, **k):
        return fade_out(*a, **k)

    @staticmethod
    def normalize(*a, **k):
        return normalize(*a, **k)

    @staticmethod
    def reverse(*a, **k):
        return reverse(*a, **k)

    @staticmethod
    def speed(*a, **k):
        return speed(*a, **k)

    @staticmethod
    def duration(*a, **k):
        return duration(*a, **k)

    @staticmethod
    def channels(*a, **k):
        return channels(*a, **k)

    @staticmethod
    def sample_rate(*a, **k):
        return sample_rate(*a, **k)

    @staticmethod
    def metadata(*a, **k):
        return metadata(*a, **k)