from .client import AIClient


def moderation(text, **kwargs):

    provider = AIClient().provider()

    return provider.moderation(
        text,
        **kwargs
    )