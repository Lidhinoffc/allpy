from .client import AIClient


def image(prompt, **kwargs):

    provider = AIClient().provider()

    return provider.image(
        prompt,
        **kwargs
    )