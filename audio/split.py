from ._compat import import_pydub

def split(input_file, start, end, save):
    """
    Extract part of an audio file.

    start/end in milliseconds.
    """
    AudioSegment = import_pydub()

    audio = AudioSegment.from_file(input_file)

    clip = audio[start:end]

    clip.export(
        save,
        format=save.split(".")[-1]
    )