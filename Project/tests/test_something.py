import pytest

import pyspark.sql.functions as F

from src.main import add_one, SuperDataTransformer
# from tests.spark_base import spark


class TestMe:

    def get_data(self, spark):
        data = [
            {'id': 1, 'name': 'abc1', 'value': 22},
            {'id': 2, 'name': 'abc1', 'value': 23},
            {'id': 3, 'name': 'def2', 'value': 33},
            {'id': 4, 'name': 'def2', 'value': 44},
            {'id': 5, 'name': 'def2', 'value': 55}
        ]
        df = spark.createDataFrame(data).coalesce(1)
        return df

    def test_always_passes(self):
        assert True

    def test_add_one(self):
        assert add_one(3) == 4

    @pytest.mark.is_spark
    def test_can_agg(self, spark):
        df = self.get_data(spark)
        trans = SuperDataTransformer()
        df_agg = trans.do_the_agg(df)

        out = df_agg.sort('name', 'sumval').collect()

        assert len(out) == 2
        assert out[0]['name'] == 'abc1'
        assert out[1]['sumval'] == 132

    @pytest.mark.is_spark
    def test_can_do_other_agg(self, spark):
        df = self.get_data(spark)
        trans = SuperDataTransformer()
        df_agg = trans.do_the_other_agg(df)

        assert 'maxval' in df_agg.columns

        out = df_agg.sort('name', 'maxval').collect()

        assert len(out) == 2
        assert out[0]['name'] == 'abc1'
        assert out[1]['maxval'] == 55
