# Remove HESA CAH Codes From Strings

Assuming that the data is loading into a `pandas` dataframe, where `CAH level subject` is a column containing HESA CAH codes e.g `01 Medicine and Dentistry`. This `regex` pattern removes both 2 digit and 6 digit patterns e.g `01` or `01-01-01`, use for then matching against HESA's CAH dictionary.

```python
pdf['CAH level subject'] = pdf['CAH level subject'].apply(lambda x: re.sub(pattern=r'(\d{2}\s)|(\d+\-)+(\d{2}\s)', repl='', string=x))
```
