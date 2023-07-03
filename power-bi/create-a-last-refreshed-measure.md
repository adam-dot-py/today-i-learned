# Create a last refreshed measure

This is useful to show users of reports when a report was last refreshed.

```DAX
Last Refresh = FORMAT(NOW(), "YYYY-MM-DD")
```
