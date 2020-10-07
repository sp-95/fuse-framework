"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"

import logging

from loguru import logger


class PropagateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)


logger.add(PropagateHandler(), format="{message}")
logger.add("logs/critical.log", level="CRITICAL", rotation="10MB")
logger.add("logs/error.log", level="ERROR", rotation="10MB")
logger.add("logs/warning.log", level="WARNING", rotation="10MB")
logger.add("logs/info.log", level="INFO", rotation="10MB")
logger.add("logs/debug.log", level="DEBUG", rotation="10MB")
