import fitz


def rotate(input_file, angle, save):
    """
    Rotate every page in a PDF.

    Parameters
    ----------
    input_file : str
    angle : int
        90, 180 or 270
    save : str
    """

    pdf = fitz.open(input_file)

    for page in pdf:
        page.set_rotation(angle)

    pdf.save(save)

    pdf.close()