from PIL import Image

def crop(input_file, box, save):
    """
    Crop an image.

    Parameters:
    - input_file: path of image
    - box: (left, upper, right, lower)
    - save: output file name
    """
    img = Image.open(input_file)
    img = img.crop(box)
    img.save(save)