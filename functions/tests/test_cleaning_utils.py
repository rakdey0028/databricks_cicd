#%pip install pytest=6.2.5
from pyspark.sql import Row, SparkSession
import pandas as pd
from datetime import datetime
import pytest
#from databricks.connect import DatabricksSession



from functions.cleaning_utils import *
@pytest.fixture(scope="session")
def spark() -> SparkSession:
  # Create a SparkSession (the entry point to Spark functionality) on
  # the cluster in the remote Databricks workspace. Unit tests do not
  # have access to this SparkSession by default.
  return SparkSession.builder.getOrCreate()


from pyspark.sql.types import *
@pytest.mark.usefixtures("spark")
def test_findtotalfunc():
  spark=SparkSession.builder.getOrCreate() #DatabricksSession.builder.getOrCreate() #
  cSchema = StructType([StructField("value", ArrayType(IntegerType()))])
  df=spark.createDataFrame(([[3,7,10]],),schema=cSchema)
  output_df = find_total(
        df
    )
  print(output_df)
  #assert isinstance(output_df, int)
  assert output_df == 20  # 4 15-min intervals over 1 hr window.