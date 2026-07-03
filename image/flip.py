from PIL import Image

def flip(input_file, mode, save):
    """
    Flip an image.

    Parameters:
    - input_file: path of image
    - mode: "horizontal" or "vertical"
    - save: output file name
    """

    img = Image.open(input_file)

    if mode == "horizontal":
        img = img.transpose(Image.FLIP_LEFT_RIGHT)

    elif mode == "vertical":
        img = img.transpose(Image.FLIP_TOP_BOTTOM)

    else:
        raise ValueError("mode must be 'horizontal' or 'vertical'")

    img.save(save)