# Using subplots

We can plot multiple graphs in one image using `plt.subplots()`. This allows us to compare variables in the same chart or create small multiples.

## Plotting on the same visuals

```python
import pandas
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

df[df['Location'] == 'United Kingdom'].plot(x='Time', y='PopTotal', ax=ax, label='United Kingdom')
df[df['Location'] == 'Germany'].plot(x='Time', y='PopTotal', ax=ax, label='Germany')

ax.set_title("UK and Germany")
plt.tight_layout()
plt.show()
```

![plt.subplot example 1](/graph_examples/plt_subplots_1.png)

In this example we are passing the two datasets to `plot` but assigning `ax` to both.

## Plotting on multiple visuals

```python
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True) # use tuples for multiple ax

# UK
df[df['Location'] == 'United Kingdom'].plot(x='Time', y='PopTotal', ax=ax1, legend=False)
ax1.set_title("UK")

# Germany
df[df['Location'] == 'Germany'].plot(x='Time', y='PopTotal', ax=ax2, legend=False)
ax2.set_title("Germany")

# Italy
df[df['Location'] == 'Italy'].plot(x='Time', y='PopTotal', ax=ax3, legend=False)
ax3.set_title("Italy")

plt.tight_layout()
plt.show()
```

![plt.subplot example 2](/graph_examples/plt_subplots_2.png)

In this example we are passing multiple `ax` to a tuple and using `nrows` and `ncols` to ask for two rows of graphs, each with one column.

## Expanding `nrows` and `ncols`

We can take this a step further for any number of visuals:

```python
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True, figsize=(10,5)) # use tuples for multiple ax

# UK
df[df['Location'] == 'United Kingdom'].plot(x='Time', y='PopTotal', ax=ax1, legend=False)
ax1.set_title("UK")

# Germany
df[df['Location'] == 'Germany'].plot(x='Time', y='PopTotal', ax=ax2, legend=False)
ax2.set_title("Germany")

# Italy
df[df['Location'] == 'Italy'].plot(x='Time', y='PopTotal', ax=ax3, legend=False)
ax3.set_title("Italy")

df[df['Location'] == 'Belgium'].plot(x='Time', y='PopTotal', ax=ax4, legend=False)
ax4.set_title("Belgium")

# Germany
df[df['Location'] == 'France'].plot(x='Time', y='PopTotal', ax=ax5, legend=False)
ax5.set_title("France")

# Italy
df[df['Location'] == 'Sweden'].plot(x='Time', y='PopTotal', ax=ax6, legend=False)
ax6.set_title("Sweden")

plt.tight_layout()
plt.show()
```

![plt.subplots example 3](/graph_examples/plt_subplots_3.png)

## Using loops and `plt.subplot`

We can make this more efficient by using `plt.subplot` in a loop:

```python
df = df.loc[df['Location'].isin(['United Kingdom', 'Italy', 'Belgium'])]

print(len(df.groupby('Location'))) # 3 countries to loop over

plot_number = 1
for countryname, selection in df.groupby("Location"):
    ax = plt.subplot(3, 1, plot_number) # nrows, ncols, index
    selection.plot(x='Time', y='PopTotal', ax=ax, label=countryname, legend=False)
    ax.set_title(countryname)
    plot_number += 1

plt.tight_layout()
```

![plt.subplots example 4](/graph_examples/plt_subplots_4.png)

## Using loops and `plt.subplots`

It can be more efficient still using `plt.subplots`. We make use of flattening nested lists using list comprehension, you can read on how to do this [here.](/Python/flatten_nested_lists.md)

```python
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
# We need to flatten axes to make it easier to loop over
# as it's current format is nested
axes_list = [item for sublist in axes for item in sublist]

first_year = df['Time'].min()
last_year = df['Time'].max()

for countryname, selection in df.groupby('Location'):
    ax = axes_list.pop(0)
    selection.plot(x='Time', y='PopTotal', label=countryname, ax=ax, legend=False)
    ax.set_title(countryname)

for ax in axes_list: # remove any unused plot
    ax.remove()

plt.tight_layout()
```

![plt.subplots example 5](/graph_examples/plt_subplots_5.png)
