import fitz


def metadata(input_file):
    """
    Return PDF metadata.
    """

    pdf = fitz.open(input_file)

    data = pdf.metadata

    pdf.close()

    return data


def page_count(input_file):
    """
    Return total pages.
    """

    pdf = fitz.open(input_file)

    total = len(pdf)

    pdf.close()

    return total

def page_size(input_file, page=0):
    """
    Return width and height of a page.
    """

    pdf = fitz.open(input_file)

    p = pdf[page]

    size = (
        p.rect.width,
        p.rect.height
    )

    pdf.close()

    return size