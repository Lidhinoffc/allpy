import allkitpy


def test_parse_html():

    html = """

    <html>

    <title>Allkitpy</title>

    </html>

    """

    assert allkitpy.web.title(html) == "Allkitpy"