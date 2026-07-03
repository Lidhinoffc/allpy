from ._compat import import_pydub


def duration(input_file):
    """
    Duration in seconds.
    """
    AudioSegment = import_pydub()

    audio = AudioSegment.from_file(input_file)

    return len(audio) / 1000


def channels(input_file):
    """
    Number of channels.
    """
    AudioSegment = import_pydub()
    audio = AudioSegment.from_file(input_file)

    return audio.channels


def sample_rate(input_file):
    """
    Sample rate.
    """
    AudioSegment = import_pydub()
    audio = AudioSegment.from_file(input_file)

    return audio.frame_rate


def metadata(input_file):
    """
    Basic audio metadata.
    """
    AudioSegment = import_pydub()
    audio = AudioSegment.from_file(input_file)

    return {
        "duration": len(audio) / 1000,
        "channels": audio.channels,
        "sample_rate": audio.frame_rate,
        "frame_width": audio.frame_width
    }