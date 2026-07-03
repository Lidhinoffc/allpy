from .client import AIClient


def chat(prompt, **kwargs):

    client = AIClient()

    provider = client.provider()

    return provider.chat(
        prompt,
        **kwargs
    )