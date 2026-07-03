from PIL import Image

def convert(input_file, mode, save):
    """
    Convert image color mode.

    Parameters:
    - input_file: image path
    - mode: "grayscale" or "RGB"
    - save: output file
    """

    img = Image.open(input_file)

    if mode == "grayscale":
        img = img.convert("L")

    elif mode == "RGB":
        img = img.convert("RGB")

    else:
        raise ValueError("mode must be 'grayscale' or 'RGB'")

    img.save(save)