# Create a random DataFrame

Creating a random DataFrame is useful for testing or plotting purposes.

```python
df = pd.DataFrame(np.random.randint(0,100, size=(5,4)), columns=list('ABCD'))
```

|   A |   B |   C |   D |
|----:|----:|----:|----:|
|  18 |  93 |  48 |  89 |
|  52 |  27 |  41 |  51 |
|  27 |  60 |  80 |  90 |
|   9 |  58 |  36 |  31 |
|  42 |   7 |  89 |  14 |