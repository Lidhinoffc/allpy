from ._compat import import_pydub


def trim(input_file, start, end, save):
    """
    Trim audio.
    """
    AudioSegment = import_pydub()
    audio = AudioSegment.from_file(input_file)

    trimmed = audio[start:end]

    trimmed.export(
        save,
        format=save.split(".")[-1]
    )