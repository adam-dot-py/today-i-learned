# Create a last refresh measure

When working in Power BI, it can be useful to indicate on your dashboard when a refresh last took place. It helps users understand the freshness of data.

To do this, you can use the below:

```dax
Last Refresh = 
VAR LastRefresh = MAX('attendance-report'[LoadDate])
RETURN
"Data last refreshed on " & FORMAT(LastRefresh, "DD/MM/YYYY") & " at " & FORMAT(LastRefresh, "HH:MM:SS")
```
