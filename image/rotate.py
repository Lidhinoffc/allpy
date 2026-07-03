from PIL import Image

def rotate(input_file, angle, save, expand=True):
    """
    Rotate an image.

    Parameters:
    - input_file: path of image
    - angle: degrees to rotate (e.g. 90, 180, 45)
    - save: output file name
    - expand: whether to resize canvas to fit rotated image
    """
    img = Image.open(input_file)
    img = img.rotate(angle, expand=expand)
    img.save(save)