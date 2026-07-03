PLUGINS = {}

def register(name, module):
    PLUGINS[name] = module

def get_plugin(name):
    return PLUGINS.get(name)

def list_plugins():
    return list(PLUGINS.keys())