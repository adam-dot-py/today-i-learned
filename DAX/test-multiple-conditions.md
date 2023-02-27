# Test multiple conditions

Using the `SWITCH()`, `TRUE()` and `AND()` we can test multiple conditions on a column and return a result. In the below example, we are assigning an age group based on the age of a person:

```dax
Age Group = SWITCH( TRUE(),
    AND( [Age]>17, [Age]<28 ), "18-27",
    AND( [Age]>27, [Age]<36 ), "28-35",
    AND( [Age]>35, [Age]<44 ), "36-43",
    AND( [Age]>43, [Age]<51 ), "44-50",
    [Age]>50, "50+", BLANK()
)
```
