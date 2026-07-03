CONFIG = {
    "debug": False,
    "version": "0.1.0",
    "log_level": "INFO"
}

def set_config(key, value):
    CONFIG[key] = value

def get_config(key, default=None):
    return CONFIG.get(key, default)