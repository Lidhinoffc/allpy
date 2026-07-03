import allkitpy
from PIL import Image
import tempfile
import os


def test_resize():

    tmp = tempfile.gettempdir()

    source = os.path.join(tmp, "photo.png")

    output = os.path.join(tmp, "result.png")

    Image.new("RGB", (200, 200)).save(source)

    allkitpy.image.resize(
    source,
    (100, 100),
    output,
)

    img = Image.open(output)

    assert img.size == (100, 100)