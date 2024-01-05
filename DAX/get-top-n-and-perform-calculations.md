# Get TOPN and perform calculations

When doing analysis, we may want to ringfence a large dataset to the top *something*, that being the top 10 or top 100. This is really useful for creating measures that are based on ring-fenced data.

```dax
MedianInternationalOutlook = 
VAR top_100 = TOPN(100, ALL('the-2024'), 'the-2024'[Overall], DESC)
RETURN
MEDIANX(top_100, 'the-2024'[InternationalOutlook])
```

In this example, I wanted to find the median `International Outlook` value for just the top 100 univerisities based on their `Overall` score. I also wanted it to not be affected by any of the filters, so applied the `ALL()` function within the `TOPN` function.

`TOPN` works like this:

`TOPN(<top value>, <table>, <value to base on>, <order>)`
