from lxml import etree


def read(filename):
    """
    Read XML.
    """

    return etree.parse(filename)


def write(tree, filename):
    """
    Save XML.
    """

    tree.write(
        filename,
        pretty_print=True,
        xml_declaration=True,
        encoding="utf-8"
    )