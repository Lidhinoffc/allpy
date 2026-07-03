from PIL import Image, ImageFilter

def blur(input_file, radius, save):
    """
    Apply blur effect to an image.

    Parameters:
    - input_file: path of image
    - radius: strength of blur (1 = light, 5+ = strong)
    - save: output file name
    """
    img = Image.open(input_file)
    img = img.filter(ImageFilter.GaussianBlur(radius))
    img.save(save)