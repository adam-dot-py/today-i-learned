# Creating schemas

When converting DataFrames to spark DataFrames, we need to create a schema to define the data structure, with column names, data types and a flag to indicate whether it is nullable or not. To create a schema, we need to make use of `StructType` and `StructField`.

The below example is an schema used for the Guardian League Table Data.

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import concat, col
from pyspark.sql.types import StructType,StructField, StringType, IntegerType, DateType, FloatType

schema = StructType([ \
    StructField("Nameofprovider",StringType(),True), \
    StructField("AverageTeachingScore",StringType(),True), \
    StructField("rank2017",StringType(),True), \
    StructField("rank2018",StringType(), True), \
    StructField("rank2019",StringType(), True), \
    StructField("rank2020",IntegerType(), True), \
    StructField("rank2021",IntegerType(), True), \
    StructField("rank2022",IntegerType(),True), \
    StructField("SatisfiedwithTeaching",StringType(),True), \
    StructField("Satisfiedwithcourse",StringType(),True), \
    StructField("Continuation",FloatType(),True), \
    StructField("Expenditureperstudentfte",FloatType(),True), \
    StructField("Studentstaffratio",FloatType(),True), \
    StructField("Careerprospects",IntegerType(),True), \
    StructField("Valueaddedscore10",FloatType(),True), \
    StructField("AverageEntryTariff",IntegerType(),True), \
    StructField("SatisfiedwithAssessment",StringType(),True) \
  ])
```
