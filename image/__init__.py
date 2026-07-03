from .resize import resize
from .crop import crop
from .rotate import rotate
from .flip import flip
from .blur import blur
from .convert import convert
from .thumbnail import thumbnail
from .compress import compress

from .utils import validate_file


class Image:
    @staticmethod
    def resize(*a, **k): return resize(*a, **k)

    @staticmethod
    def crop(*a, **k): return crop(*a, **k)

    @staticmethod
    def rotate(*a, **k): return rotate(*a, **k)

    @staticmethod
    def flip(*a, **k): return flip(*a, **k)

    @staticmethod
    def blur(*a, **k): return blur(*a, **k)

    @staticmethod
    def convert(*a, **k): return convert(*a, **k)

    @staticmethod
    def thumbnail(*a, **k): return thumbnail(*a, **k)

    @staticmethod
    def compress(*a, **k): return compress(*a, **k)