import fitz
import os


def extract_images(input_file, output_folder):
    """
    Extract all images from a PDF.
    """

    os.makedirs(output_folder, exist_ok=True)

    pdf = fitz.open(input_file)

    image_number = 1

    for page_index in range(len(pdf)):

        page = pdf[page_index]

        images = page.get_images(full=True)

        for img in images:

            xref = img[0]

            base = pdf.extract_image(xref)

            image = base["image"]

            ext = base["ext"]

            filename = os.path.join(
                output_folder,
                f"image_{image_number}.{ext}"
            )

            with open(filename, "wb") as f:
                f.write(image)

            image_number += 1

    pdf.close()