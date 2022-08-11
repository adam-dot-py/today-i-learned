# `VLOOKUP()` with multiple conditions

`VLOOKUP()` cannot natively handle multiple criteria, however you can make use of a helper column if you have access to the source data.

Consider the below scenario:

![vlookup with multiple criteria](/supporting-images/vlookup-multiple-criteria.png)

You could use the formula `=VLOOKUP(I4&I5,4,0)` to return the `Department` for `JonVictor` (the created helper column).

The syntax for this is `=VLOOKUP(val1&val2, data,column,match_type)`.