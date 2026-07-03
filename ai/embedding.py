from .client import AIClient


def embedding(text, **kwargs):

    provider = AIClient().provider()

    return provider.embedding(
        text,
        **kwargs
    )