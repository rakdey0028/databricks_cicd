#%pip install pytest=6.2.5
from pyspark.sql import Row, SparkSession
import pandas as pd
from datetime import datetime
import pytest
import os
from databricks.connect import DatabricksSession



from functions.cleaning_utils import *
@pytest.fixture(scope="session")
def spark() -> SparkSession:
  # Create a SparkSession (the entry point to Spark functionality) on
  # the cluster in the remote Databricks workspace. Unit tests do not
  # have access to this SparkSession by default.
  is_ci = os.getenv("GITHUB_ACTIONS") == "true"
  if is_ci:
    return DatabricksSession.builder.getOrCreate()
  else:  
    return SparkSession.builder.getOrCreate()


from pyspark.sql.types import *
@pytest.mark.usefixtures("spark")
def test_findtotalfunc(spark):
  #spark=DatabricksSession.builder.getOrCreate() #SparkSession.builder.getOrCreate() 
  cSchema = StructType([StructField("value", ArrayType(IntegerType()))])
  df=spark.createDataFrame(([[3,7,45]],),schema=cSchema)
  output_df = find_total(
        df
    )
  print(output_df)
  #assert isinstance(output_df, int)
  assert output_df == 58  # 4 15-min intervals over 1 hr window.

@pytest.mark.usefixtures("spark")
def test_can_agg(spark):
  data = [
            {'id': 1, 'name': 'abc1', 'value': 22},
            {'id': 2, 'name': 'abc1', 'value': 23},
            {'id': 3, 'name': 'def2', 'value': 33},
            {'id': 4, 'name': 'def2', 'value': 44},
            {'id': 5, 'name': 'def2', 'value': 55}
        ]
  df = spark.createDataFrame(data).coalesce(1)
  df_agg = do_the_agg(df)

  assert 'sumval' in df_agg.columns

  out = df_agg.sort('name', 'sumval').collect()

  assert len(out) == 2
  assert out[0]['name'] == 'abc1'
  assert out[1]['sumval'] == 132
