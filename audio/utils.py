from ._compat import import_pydub

def export(audio, save):
    """
    Export AudioSegment.
    """

    audio.export(
        save,
        format=save.split(".")[-1]
    )