# Calculate age in Excel

Calculating age can be done via the `DATEDIF()` function.

## Example

`=DATEDIF(date, date_to_compare, format)`

To calculate the age of someone to date, you can pass `TODAY()` as the date to compare against. You can pass "y" as the format to indicate the difference in `years`. You can pass other arguments like "d" (days) or "m" (months) or a combination for other results.

`=DATEDIF(date, TODAY(), "y")`
