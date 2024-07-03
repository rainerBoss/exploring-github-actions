import logging.handlers
import sys
import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
handler = logging.handlers.TimedRotatingFileHandler("logs/app.log", when="midnight", backupCount=7, delay=True)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel("DEBUG")


def greet(name):
    logger.debug(f"Calling function `greet` with argument `{name}`")
    return f"Hello, {name}"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(greet(sys.argv[1]))
    else:
        logger.warning("No arguments were provided")