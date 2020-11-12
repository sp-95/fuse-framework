import logging

import pytest
from _pytest.logging import LogCaptureFixture, _LiveLoggingNullHandler
from loguru import logger

from {{cookiecutter.project_slug}}.logger import log_config


@pytest.fixture
def caplog(caplog: LogCaptureFixture) -> LogCaptureFixture:
    class PropagateHandler(logging.Handler):
        def emit(self, record: logging.LogRecord) -> None:
            logging.getLogger(record.name).handle(record)

    log_config.setup(suppress_handlers=False)
    logging.getLogger().handlers = [_LiveLoggingNullHandler()]
    handler_id = logger.add(PropagateHandler(), format="{message}")
    yield caplog
    logger.remove(handler_id)
