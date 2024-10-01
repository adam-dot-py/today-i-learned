# Piping outputs of cmdlets

You can pipe the output of a cmdlet into another cmdlet, for example:

```powershell
$files = dir
$files | where length -gt 10000
```

This pipes the output of `$files` to the `where` cmdlet (in this case, `Where-Object` is aliased) and then uses the `-gt` operator (greater than) to show only files bigger than 10000 bytes.

This functionality allows for powerful use cases.