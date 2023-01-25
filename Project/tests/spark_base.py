import pytest
from pyspark.sql import SparkSession
import logging

logger = logging.getLogger('sparkTesting')

def get_spark():
    spark = SparkSession.builder\
        .master("local[*]") \
        .appName('sparkTesting') \
        .getOrCreate()

    return spark

# @pytest.fixture()
# def spark():
#     # print("spark setup")
#     logger.info("spark setup")
#     spark_session = get_spark()
#     yield spark_session
#     logger.info("teardown")
#     # print("teardown")
