import allkitpy


def test_upper():

    assert allkitpy.text.upper("hello") == "HELLO"


def test_lower():

    assert allkitpy.text.lower("HELLO") == "hello"


def test_title():

    assert allkitpy.text.title("hello world") == "Hello World"


def test_capitalize():

    assert allkitpy.text.capitalize("hello") == "Hello"


def test_word_count():

    assert allkitpy.text.word_count("one two three") == 3