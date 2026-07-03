from .config import provider
from .registry import get

from .exceptions import (
    ProviderNotConfigured,
    ProviderNotSupported,
)


class AIClient:

    def provider(self):

        name = provider()

        if name is None:
            raise ProviderNotConfigured(
                "Configure a provider first."
            )

        cls = get(name)

        if cls is None:
            raise ProviderNotSupported(name)

        return cls()