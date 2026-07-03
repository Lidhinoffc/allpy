from PIL import Image


def resize(input_file, size, save):
    """
    Resize an image.

    Parameters
    ----------
    input_file : str
        Input image path.
    size : tuple[int, int]
        (width, height)
    save : str
        Output image path.
    """
    img = Image.open(input_file)
    img = img.resize(size)
    img.save(save)