# Powershell Comparison Operators

## Greater than or less than

Use the `-gt` operator for greater than and `-lt` operator for less than.

```powershell
$a = 10
$b = 5

$a -gt $b
```

Output would be `True`.

# String Matching

If ignoring case, you can use `-match` to look for a given string in another string. If case-sensitive is required, use `-cmatch`.

```powershell
"My name is Adam" -match "Adam"
```

Output would be `True`.

```powershell
"My name is Adam" -cmatch "ADAM"
```

Output would be `False`.

## Like Matching


