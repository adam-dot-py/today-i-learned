# Using lambda with if, elif and else conditions

You can use lambda functions with the `apply` function to return a value based on conditions.

```python
test = lambda x : True if (x > 10 and x < 20) else False

print(test(12))
print(test(3))
print(test(24))
```

True
False
False

`True` and `False` can be replaced with text values, for example for determining if a margin of error falls between an acceptable boundary of 4 percent  to 8 percent:

```python
question_scale_df['margin_of_error'] = (question_scale_df.pctAgree - question_scale_df.ci_lower).apply(lambda x: 'acceptable' if (x >= 4.0 and x <=8.0) else 'not acceptable')
```

## Using lambda as if, elseif and else

You can use lambda to perform if, elif and else conditions:

```python
df['Type'] = df.Weighting.apply(lambda x: "Promoter" if x >= 9 else ("Detractor" if x <= 6 else "Passive"))
```

This says if x is greater than or equal to 9 then Promoter, else if x is less than or equal to 6 then Detractor else Passive.
