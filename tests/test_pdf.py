import allkitpy
import os
import tempfile


def test_create_pdf():

    tmp = tempfile.gettempdir()

    filename = os.path.join(
        tmp,
        "sample.pdf"
    )

    allkitpy.pdf.create(
        filename,
        text="Hello"
    )

    assert os.path.exists(filename)