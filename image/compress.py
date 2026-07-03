from PIL import Image

def compress(input_file, quality, save):
    """
    Compress image by reducing quality.

    Parameters:
    - input_file: image path
    - quality: 1–100 (lower = smaller file)
    - save: output file
    """
    img = Image.open(input_file)
    img.save(save, quality=quality, optimize=True)