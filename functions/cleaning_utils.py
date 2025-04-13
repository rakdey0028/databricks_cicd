#from pyspark.sql import DataFrame, functions as F

from pyspark.sql.types import *
import pyspark.sql.functions  as F
def find_total(df):
  df = df.withColumn(
      "Total",
      F.aggregate("value", F.lit(0), lambda acc, x: acc + x)
  )
  return df.select('Total').collect()[0][0]