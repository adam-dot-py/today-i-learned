# Get and create aliases

Aliases allow you to easily call on a cmdlet in a another form, for example:

```powershell
get-alias ls
```

Would return the cmdlet `Get-ChildItem`. `ls` can be used to invoke the cmdlet.

You can also set a cmdlet to a given alias, for example:

```powershell
set-alias blah Get-ChildItem
```

When calling `blah` the cmdlet `Get-ChildItem` would be invoked. 