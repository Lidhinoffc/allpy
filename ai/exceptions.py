class AIError(Exception):
    """
    Base AI exception.
    """
    pass


class ProviderNotConfigured(AIError):
    pass


class ProviderNotSupported(AIError):
    pass


class APIKeyMissing(AIError):
    pass