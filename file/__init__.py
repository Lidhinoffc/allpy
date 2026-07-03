from .ops import copy, move, delete, rename
from .info import exists, size, list_dir

class File:
    @staticmethod
    def copy(*a, **k): return copy(*a, **k)

    @staticmethod
    def move(*a, **k): return move(*a, **k)

    @staticmethod
    def delete(*a, **k): return delete(*a, **k)

    @staticmethod
    def rename(*a, **k): return rename(*a, **k)

    @staticmethod
    def exists(*a, **k): return exists(*a, **k)

    @staticmethod
    def size(*a, **k): return size(*a, **k)

    @staticmethod
    def list_dir(*a, **k): return list_dir(*a, **k)