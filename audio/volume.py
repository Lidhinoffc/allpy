from ._compat import import_pydub


def increase(input_file, db, save):
    """
    Increase volume.
    """
    AudioSegment = import_pydub()
    audio = AudioSegment.from_file(input_file)

    audio += db

    audio.export(
        save,
        format=save.split(".")[-1]
    )


def decrease(input_file, db, save):
    """
    Decrease volume.
    """
    AudioSegment = import_pydub()

    audio = AudioSegment.from_file(input_file)

    audio -= db

    audio.export(
        save,
        format=save.split(".")[-1]
    )