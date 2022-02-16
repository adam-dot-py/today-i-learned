# Format Floats

You can use `pd.options.display.float_format` to change the display of float numbers in a dataframe, useful for when scientific notation is used by default by Pandas. 

`pd.options.display.float_format == '{:, .2f}'.format`, where the comma is the seperator for thousands. 