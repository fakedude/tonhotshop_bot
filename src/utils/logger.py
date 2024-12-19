import logging
import os

from config import LOG_LEVEL


class LoggerFormatterBuilder():
    _is_debug: bool = False
    _is_systemd: bool = False
    _date_fmt = '%Y-%m-%d %H:%M:%S'

    def set_debug(self, value: bool):
        self._is_debug = value

    def set_systemd(self, value: bool):
        self._is_systemd = value

    def build(self):
        fmt = (f"{None if self._is_systemd else '%(asctime)s.%(msecs)03d'} [%(levelname)s] "
               f"{'[%(name)s.%(funcName)s]' if self._is_debug else '[%(name)s]'} %(message)s")
        return logging.Formatter(fmt) if self._is_systemd else logging.Formatter(fmt, self._date_fmt)


# define custom log level names
log_levels = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warn': logging.WARNING,
    'error': logging.ERROR
}


logging.addLevelName(logging.DEBUG, 'debug')
logging.addLevelName(logging.INFO, 'info ')
logging.addLevelName(logging.WARNING, 'warn ')
logging.addLevelName(logging.ERROR, 'error')

log_level = log_levels.get(LOG_LEVEL, logging.DEBUG)

formatter_builder = LoggerFormatterBuilder()
formatter_builder.set_debug(log_level == logging.DEBUG)
formatter_builder.set_systemd(os.getppid() == 1)

global_formatter = formatter_builder.build()
global_handler = logging.StreamHandler()
global_handler.setFormatter(global_formatter)


def logger_factory(name: str):
    name_logger = logging.getLogger(name)

    for handler in name_logger.handlers:
        name_logger.removeHandler(handler)

    name_logger.setLevel(log_level)
    name_logger.addHandler(global_handler)

    return name_logger


def init_module_loggers(*args: str):
    for logger_name in args:
        logger = logging.getLogger(logger_name)

        for handler in logger.handlers:
            logger.removeHandler(handler)

        logger.setLevel(log_level)
        logger.addHandler(global_handler)
