
from ._compat import import_pydub


def fade_in(input_file, milliseconds, save):
    """
    Apply fade-in effect.
    
    """
    AudioSegment = import_pydub()

    audio = AudioSegment.from_file(input_file)

    audio = audio.fade_in(milliseconds)

    audio.export(
        save,
        format=save.split(".")[-1]
    )


def fade_out(input_file, milliseconds, save):
    """
    Apply fade-out effect.
    """
    AudioSegment = import_pydub()
    audio = AudioSegment.from_file(input_file)

    audio = audio.fade_out(milliseconds)

    audio.export(
        save,
        format=save.split(".")[-1]
    )


def normalize(input_file, save):

    AudioSegment = import_pydub()

    from pydub.effects import normalize as _normalize

    audio = AudioSegment.from_file(input_file)

    audio = _normalize(audio)

    audio.export(
        save,
        format=save.split(".")[-1]
    )