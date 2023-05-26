import logging


class Logger(logging.Logger):
    def __init__(self, name: str):
        super().__init__(name)
        logging.TRACE = logging.DEBUG - 1
        logging.addLevelName(logging.TRACE, "TRACE")
        self._l = logging.getLogger(name)
        self._l.setLevel(logging.TRACE)

    def trace(self, msg: str):
        self._l.log(logging.TRACE, msg)
