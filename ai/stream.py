from .client import AIClient


def stream(prompt, **kwargs):

    provider = AIClient().provider()

    return provider.stream(
        prompt,
        **kwargs
    )