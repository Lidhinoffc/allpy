import os


def size(filename):
    """
    File size.
    """

    return os.path.getsize(filename)


def exists(filename):

    return os.path.exists(filename)


def extension(filename):

    return os.path.splitext(filename)[1]