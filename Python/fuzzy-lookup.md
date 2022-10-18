# Fuzzy lookup in Python

We can do fuzzy lookup using the `difflib` library, which is part of the standard library in Python.

```python
import difflib
my_str = 'apple'
str_list = ['ape' , 'fjsdf', 'aerewtg', 'dgyow', 'paepd']
best_match = difflib.get_close_matches(word=my_str,possibilities=str_list,n=1)[0]
score = difflib.SequenceMatcher(None, my_str, best_match).ratio()

for word in str_list:
    print ("score for: " + my_str + " vs. " + word + " = " + str(difflib.SequenceMatcher(None, my_str, word).ratio()))
```

Score for: apple vs. ape = 0.75 \
Score for: apple vs. fjsdf = 0.0 \
Score for: apple vs. aerewtg = 0.3333333333333333 \
Score for: apple vs. dgyow = 0.0 \
Score for: apple vs. paepd = 0.4
