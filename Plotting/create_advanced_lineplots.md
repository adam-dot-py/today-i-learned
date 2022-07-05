# Creating Advanced Lineplots

The following can be used to create an advanced lineplot, utilising [matplotlib.dates] and other advanced `matplotlib` features: 

```python
df = pd.read_csv(r'\example_datasets\frankfurt_weather.csv')
df['time'] = pd.to_datetime(df['time'], format = '%Y-%m-%d %H:%M')

plt.rcParams['font.size'] = 18
fig, ax = plt.subplots(figsize = (20,5))

ax.plot(df['time'], df['air_temperature'], label = 'Air temperature at Frankfurt Int. Airport in 2015')

ax.legend()
ax.set_ylabel('Temperature (°C)')

# x axis limits to the start of the year to the end
ax.set_xlim([pd.to_datetime('2015-01-01', format = '%Y-%m-%d'),
             pd.to_datetime('2015-12-31', format = '%Y-%m-%d')])

 # x ticks' labels format and position with matplotlib.dates
 # changes the date format to just the month name and shows all months
ax.xaxis.set_major_locator(md.MonthLocator(interval = 1))
ax.xaxis.set_major_formatter(md.DateFormatter('%b'))

# capital first letter of x ticks' labels for months' names
fig.canvas.draw()
ax.set_xticklabels([month.get_text().title() for month in ax.get_xticklabels()])

plt.tight_layout()
plt.show()
```

![advanced line plot example](/graph_examples/frankfurt_weather.jpg)
