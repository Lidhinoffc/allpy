from ._compat import import_pydub


def merge(files, save):
    """
    Merge multiple audio files.
    """
    AudioSegment = import_pydub()
    result = AudioSegment.empty()

    for file in files:
        result += AudioSegment.from_file(file)

    result.export(
        save,
        format=save.split(".")[-1]
    )