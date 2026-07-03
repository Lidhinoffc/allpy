import datetime

def log(message, level="INFO"):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{time}] [{level}] Allkitpy: {message}")

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger("allkitpy")