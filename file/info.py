import os

def exists(path):
    return os.path.exists(path)

def size(path):
    return os.path.getsize(path)

def list_dir(path):
    return os.listdir(path)