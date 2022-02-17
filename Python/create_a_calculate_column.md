# Create a calculated column 

In Pandas, we have the freedom to add different functions whenever needed like lambda function, sort function, etc. We can apply a lambda function to both the columns and rows of the Pandas data frame.

**Example**

```python
# importing pandas library
import pandas as pd
   
# creating and initializing a list
values= [['Rohan',455],['Elvish',250],['Deepak',495],
         ['Soni',400],['Radhika',350],['Vansh',450]] 
  
# creating a pandas dataframe
df = pd.DataFrame(values,columns=['Name','Total_Marks'])
  
# Applying lambda function to find 
# percentage of 'Total_Marks' column 
# using df.assign()
df = df.assign(Percentage = lambda x: (x['Total_Marks'] /500 * 100))
  
# displaying the data frame
df
```