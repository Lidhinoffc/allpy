from . import csv
from . import excel
from . import json_file
from . import xml
from . import yaml_file

from .info import (
    size,
    exists,
    extension
)


class Data:

    csv = csv
    excel = excel
    json = json_file
    xml = xml
    yaml = yaml_file

    @staticmethod
    def size(*a, **k):
        return size(*a, **k)

    @staticmethod
    def exists(*a, **k):
        return exists(*a, **k)

    @staticmethod
    def extension(*a, **k):
        return extension(*a, **k)