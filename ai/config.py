"""
Global AI configuration.
"""

_provider = None
_api_key = None
_base_url = None
_model = None


def configure(
    provider=None,
    api_key=None,
    base_url=None,
    model=None,
):
    global _provider
    global _api_key
    global _base_url
    global _model

    if provider is not None:
        _provider = provider

    if api_key is not None:
        _api_key = api_key

    if base_url is not None:
        _base_url = base_url

    if model is not None:
        _model = model


def provider():
    return _provider


def api_key():
    return _api_key


def base_url():
    return _base_url


def model():
    return _model