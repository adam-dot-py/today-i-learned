# Subtract previous value

Where we have a table like the below:

| Date         | Apps - Daily        | Apps Change      |
|-------------:|--------------------:|------------------|
| 01/10/2022   | 48                  | 2                |
| 02/10/2022   | 50                  | 2                |
| 03/10/2022   | 55                  | 5                |

and we want to find the daily change in the `Apps - Daily` value, we can use the following DAX:

```dax
Apps Daily = 
// Get daily applications change
VAR _appsDaily = CALCULATE(
    AllMeasures[Apps - Daily] - 
    CALCULATE( AllMeasures[Apps - Daily)], 
    DATEADD( 'Date'[Date], - 1, DAY )
    )
)
RETURN
IF( ISBLANK( AllMeasures[Applications (Daily)] ), BLANK(), _appsDaily )
```
