from .client import AIClient


def vision(image, prompt="", **kwargs):

    provider = AIClient().provider()

    return provider.vision(
        image,
        prompt,
        **kwargs
    )