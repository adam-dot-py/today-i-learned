# Convert a Pandas DataFrame to a Spark Dataframe

```python
class ConvertPandas():
  """
  A class to convert a Pandas DataFrame to a Spark DataFrame, automatically creating a schema by mapping Pandas datatypes to their Spark equivalent.
  
  Attributes
  --------------
  pdf : dataframe
    The Pandas DataFrame to be converted.
  
  Methods
  --------------  
  find_spark_equivalent()
    Map a Pandas datatype and return a matching Spark datatype. If no match is found, just return StringType()
    
  organise_structure(column_name, format_type)
    Iterate through the Pandas datatypes and replace them with a matching Spark datatype. If no match found, just return StringType()
  
  get_schema()
    Construct a Spark schema from Pandas datatypes, using the above methods.
  
  pandas_to_spark()
    Construct a Spark dataframe using the created schema
  """
  
  def __init__(self, pdf):
    self.pdf = pdf
    
  def find_spark_equivalent(self):
    """Maps a given Pandas datatype to the Spark datatype. If no match is found, StringType() is returned.
    
    Parameters
    --------------
    self.format_type
      The Pandas datatype.
    """
    if self.format_type == 'datetime64[ns]': 
      return TimestampType()
    elif self.format_type == 'int64': 
      return IntegerType()
    elif self.format_type  == 'int32': 
      return IntegerType()
    elif self.format_type == 'float64': 
      return DoubleType()
    elif self.format_type == 'float32': 
      return FloatType()
    else: 
      return StringType()

  def organise_structure(self, column_name, format_type):
    """Returns a StructField() containing the Pandas column (string) and datatype (format_type).
    These arguments are passed from get_schema(), in the for loop.
    
    Parameters
    --------------  
    column_name
      The Pandas column
    format_type
      The Pandas datatype
    spark_type
      The Spark datatype, mapped from the format_type
    """
    self.column_name = column_name
    self.format_type = format_type
    try: 
      spark_type = self.find_spark_equivalent()
    except: 
      spark_type = StringType()
    return StructField(column_name, spark_type)
 
  def get_schema(self):
    """Constructs a schema, or Spark StructType() by iterating over the Pandas columns and datatypes, using organise_structure() to get Spark equivalent datatypes and returning StructFields.
    StructFields() are appended to struct_list (list) and then passed to SructType().
    
    Parameters
    --------------  
    string
      The Pandas column
    format_type
      The Pandas datatype
    spark_type
      The Spark datatype, mapped from the format_type
    """
    self.columns = list(self.pdf.columns)
    self.types = list(self.pdf.dtypes)
    struct_list = []
    for column, pandas_type in zip(self.columns, self.types):
      struct_list.append(self.organise_structure(column_name=column, format_type=pandas_type))
    schema = StructType(struct_list)
    return schema
    
  def to_spark(self):
    """Constructs a Spark dataframe from a Pandas dataframe, using the class methods.
    
    Parameters
    --------------  
    self.pdf
      The Pandas dataframe
      
    self.get_schema
      The constructed schema
    """
    
    return spark.createDataFrame(self.pdf, self.get_schema())
```
