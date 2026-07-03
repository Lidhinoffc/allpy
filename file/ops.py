import os
import shutil

def copy(src, dst):
    shutil.copy2(src, dst)

def move(src, dst):
    shutil.move(src, dst)

def delete(path):
    os.remove(path)

def rename(src, dst):
    os.rename(src, dst)