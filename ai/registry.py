PROVIDERS = {}


def register(name, provider):

    PROVIDERS[name.lower()] = provider


def get(name):

    return PROVIDERS.get(name.lower())


def names():

    return sorted(PROVIDERS.keys())