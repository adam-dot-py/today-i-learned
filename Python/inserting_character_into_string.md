# Inserting a character into a string 

You can use the below example to insert a character into a string. 

To insert a character into a string at `index i`, split the string using the `slicing` syntax `a_string[:i] and a_string[i:]`.

Between these two portions of the original string, use the concatenation operator `+` to insert the desired character.

Assign the result to the variable that held the original string.

```python
a_string = 'ac'
a_string = a_string[:1] + "b" + a_string[1:]
```

The below inserts b in the the middle of `a_string`, resulting in `abc`.

I used it to insert a backslash in a stirng: 

```python
frame['Academic Year'] = filename[:4] + "/" + filename[4:].replace('.csv', '')
```

Results in `2021/22`.