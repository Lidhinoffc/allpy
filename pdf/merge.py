import fitz


def merge(pdf_files, save):
    """
    Merge multiple PDF files.

    Parameters
    ----------
    pdf_files : list[str]
        List of PDF filenames.

    save : str
        Output PDF filename.
    """

    merged = fitz.open()

    for pdf in pdf_files:
        doc = fitz.open(pdf)
        merged.insert_pdf(doc)
        doc.close()

    merged.save(save)
    merged.close()