import logging
from logger import Logger


def main():
    logger = Logger(__name__)
    logger.trace("This is a trace")
    logger.debug("Debug method")

if __name__ == "__main__":
    main()
