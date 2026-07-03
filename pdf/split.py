import fitz
import os


def split(input_file, output_folder):
    """
    Split a PDF into one PDF per page.

    Parameters
    ----------
    input_file : str
        PDF to split.

    output_folder : str
        Folder where pages will be saved.
    """

    os.makedirs(output_folder, exist_ok=True)

    pdf = fitz.open(input_file)

    for page_number in range(len(pdf)):

        new_pdf = fitz.open()

        new_pdf.insert_pdf(
            pdf,
            from_page=page_number,
            to_page=page_number
        )

        filename = os.path.join(
            output_folder,
            f"page_{page_number + 1}.pdf"
        )

        new_pdf.save(filename)
        new_pdf.close()

    pdf.close()