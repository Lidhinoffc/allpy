"""
Compatibility helpers for the audio module.
"""


def import_pydub():
    """
    Import AudioSegment only when needed.
    """

    try:
        from pydub import AudioSegment
        return AudioSegment

    except (ImportError, ModuleNotFoundError) as e:
        raise RuntimeError(
            "Audio support is unavailable.\n\n"
            "Possible reasons:\n"
            "- Pydub is not installed.\n"
            "- The installed version of Pydub does not support your Python version.\n"
            "- Required audio dependencies are missing.\n\n"
            f"Original error:\n{e}"
        ) from e