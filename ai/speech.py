from .client import AIClient


def speech(text, **kwargs):

    provider = AIClient().provider()

    return provider.speech(
        text,
        **kwargs
    )