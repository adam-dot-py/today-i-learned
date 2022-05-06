# Create scatter plot charts

Scatter graph plots are great for comparing two variables against each other on an x and y axis.

For this example, it looks ar surveying data for 2000 respondents and their unique response to two questions in a survey, `Q27` and 'Q28'.

First, we create a `pivot table` of each `RespodantId` and their response to the questions: 

```python
c_df = c_df.pivot_table('Weighting', ['RespondantId'], 'QuestionNumber', aggfunc='sum')
c_df = pd.DataFrame(c_df.to_records()) # Flatten the dataframe to access columns
```

|      |   RespondantId |   27 |   28 |
|-----:|---------------:|-----:|-----:|
|    0 |    1.14001e+11 |   10 |    5 |
|    1 |    1.14001e+11 |    7 |    4 |
|    2 |    1.14001e+11 |    8 |    4 |
|    3 |    1.14001e+11 |   10 |    5 |

Next, we want to pair up all of the possible combinations of choices within the data and count how many times these appear in our data - this will dictate the size of our scatter bubbles:

```python
counts = c_df.groupby(by=['27', '28']).size().to_frame('size').reset_index()
```

The above will get all possible combinations of responses and count how many times these appear. First we group by the required questions, then use `size` to count the number of elements. This is then passed to a `DataFrame` and given the name `size`.

|    |   27 |   28 |   size |
|---:|-----:|-----:|-------:|
|  0 |    1 |    1 |     42 |
|  1 |    1 |    2 |     16 |
|  2 |    1 |    3 |     21 |
|  3 |    1 |    4 |     12 |

Finally, we can then pass this to the `matplotlib` to create our scatter graph: 

```python
sizes = counts['size'] ** 1

sc = plt.scatter(x=counts['27'], y=counts['28'],
                 s=sizes, alpha=0.5, 
                 edgecolor='black')

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1, fancybox=True, *sc.legend_elements("sizes", num=6)) # Show the circle size representations in the legend

plt.xlabel('Net Promoter Score')
plt.ylabel('Overall satisfaction')
plt.locator_params(integer=True, tight=True) # Set the axis to an interger, no floats
plt.tight_layout()
plt.savefig("correlation.png", dpi=1000)
plt.show()
```

![Scatter graph example](/graph_examples/correlation.png)