from ._compat import import_pydub


def convert(input_file, save, format=None):
    """
    Convert audio to another format.

    Examples
    --------
    mp3 -> wav
    wav -> mp3
    ogg -> mp3
    """

    AudioSegment = import_pydub()

    audio = AudioSegment.from_file(input_file)

    if format is None:
        format = save.split(".")[-1]

    audio.export(
        save,
        format=format
    )