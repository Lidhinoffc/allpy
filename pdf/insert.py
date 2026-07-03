import fitz


def insert_pages(input_file, insert_pdf, position, save):
    """
    Insert pages from another PDF.

    position starts from 0.
    """

    pdf = fitz.open(input_file)

    extra = fitz.open(insert_pdf)

    pdf.insert_pdf(
        extra,
        start_at=position
    )

    pdf.save(save)

    extra.close()
    pdf.close()