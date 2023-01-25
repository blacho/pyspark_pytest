import pytest
import logging
from .spark_base import get_spark


logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True, scope="session")
def spark():
    # print("spark setup")
    logger.info("spark setup")
    spark_session = get_spark()
    yield spark_session
    logger.info("teardown")
    # print("teardown")