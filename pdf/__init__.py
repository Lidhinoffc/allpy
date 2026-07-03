from .create import create
from .merge import merge
from .split import split

from .extract import extract_text
from .images import extract_images

from .rotate import rotate
from .delete import delete_pages
from .insert import insert_pages
from .watermark import watermark
from .security import encrypt, decrypt
from .compress import compress



from .info import (
    metadata,
    page_count,
    page_size
)


class PDF:

    @staticmethod
    def create(*a, **k):
        return create(*a, **k)

    @staticmethod
    def merge(*a, **k):
        return merge(*a, **k)

    @staticmethod
    def split(*a, **k):
        return split(*a, **k)

    @staticmethod
    def extract_text(*a, **k):
        return extract_text(*a, **k)

    @staticmethod
    def extract_images(*a, **k):
        return extract_images(*a, **k)

    @staticmethod
    def metadata(*a, **k):
        return metadata(*a, **k)

    @staticmethod
    def page_count(*a, **k):
        return page_count(*a, **k)

    @staticmethod
    def page_size(*a, **k):
        return page_size(*a, **k)
    
    @staticmethod
    def rotate(*a, **k):
        return rotate(*a, **k)

    @staticmethod
    def delete_pages(*a, **k):
        return delete_pages(*a, **k)

    @staticmethod
    def insert_pages(*a, **k):
        return insert_pages(*a, **k)

    @staticmethod
    def watermark(*a, **k):
        return watermark(*a, **k)

    @staticmethod
    def encrypt(*a, **k):
        return encrypt(*a, **k)

    @staticmethod
    def decrypt(*a, **k):
        return decrypt(*a, **k)

    @staticmethod
    def compress(*a, **k):
        return compress(*a, **k)