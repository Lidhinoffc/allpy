from ._compat import import_pydub


def reverse(input_file, save):
    """
    Reverse audio.
    """
    AudioSegment = import_pydub()

    audio = AudioSegment.from_file(input_file)

    audio = audio.reverse()

    audio.export(
        save,
        format=save.split(".")[-1]
    )
def speed(input_file, rate, save):
    """
    Change playback speed.

    rate:
        0.5 = half speed
        2.0 = double speed
    """
    AudioSegment = import_pydub()
    audio = AudioSegment.from_file(input_file)

    audio = audio._spawn(
        audio.raw_data,
        overrides={
            "frame_rate": int(audio.frame_rate * rate)
        }
    )

    audio = audio.set_frame_rate(audio.frame_rate)

    audio.export(
        save,
        format=save.split(".")[-1]
    )