import logging
from io import StringIO
import pytest
import allure

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.fixture(scope='session', autouse=True)
def allure_logging(request):
    log_capture_string = StringIO()
    ch = logging.StreamHandler(log_capture_string)
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)

    yield

    allure.attach(log_capture_string.getvalue(), name="logs", attachment_type=allure.attachment_type.TEXT)
