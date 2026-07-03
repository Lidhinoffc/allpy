from PIL import Image

def thumbnail(input_file, size, save):
    """
    Create a thumbnail (small optimized image).
    """
    img = Image.open(input_file)
    img.thumbnail(size)
    img.save(save)