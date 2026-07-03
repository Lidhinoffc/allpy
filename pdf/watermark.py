import fitz


def watermark(input_file, text, save):
    """
    Add a centered text watermark to each page.
    """

    pdf = fitz.open(input_file)

    for page in pdf:

        rect = page.rect

        x = rect.width / 3
        y = rect.height / 2

        page.insert_text(
            (x, y),
            text,
            fontsize=36
        )

    pdf.save(save)
    pdf.close()