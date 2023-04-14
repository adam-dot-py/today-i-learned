# Change fonts

Changing fonts can be done directly in calls to different functions within `plt`, as long as the fon style is installed on the base system. However, we can also use `**` to unpack a dictionary as function arguments, like below:

```python
value_font = {'fontname' : 'Consolas'}
text_font = {'fontname' : 'Bahnschrift'}
```

This is an example usage scenario:

```python
df = pdf.pivot_table(index='College', values=['RecordId'], aggfunc='count').sort_values(by='RecordId', ascending=False)

value_font = {'fontname' : 'Consolas'}
text_font = {'fontname' : 'Bahnschrift'}

os.makedirs(os.path.join('exception-visuals', month_name), exist_ok=True)

fig, ax = plt.subplots(figsize=(6,4))
df.plot(ax=ax, kind='bar', edgecolor='black', color='#007F7B', width=0.6)
ax.bar_label(ax.containers[0], label_type='center', rotation=90, color='white', fontname='Consolas')
ax.get_legend().remove()
plt.yticks(**value_font)
plt.xticks(**text_font)
plt.xlabel(None)
plt.ylabel('Exception Count', **text_font)
plt.tight_layout()
plt.savefig(f'exception-visuals/{month_name}/{month_name}-exception-count.png', dpi=100)
plt.show()
```
