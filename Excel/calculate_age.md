# Calculate age in Excel

Calculating age can be done via the `DATEDIF()` function or via substraction.

## Example 1

`=DATEDIF(date, date_to_compare, format)`

To calculate the age of someone to date, you can pass `TODAY()` as the date to compare against. You can pass "y" as the format to indicate the difference in `years`. You can pass other arguments like "d" (days) or "m" (months) or a combination for other results.

`=DATEDIF(date, TODAY(), "y")`

## Example 2

`=INT((date - dob) / 365.25)`

To account for a leap year occurring every 4 years, 365.25 is used in the formula. We then wrap the formula in `INT` to round to the nearest integer.
