# Using Calculate with multiple conditions

The operatot `||` indicates `OR`.

```dax
Red or Contoso Sales :=
CALCULATE (
    [Sales Amount],
    'Product'[Color] = "Red" || 'Product'[Brand] = "Contoso"
)
 
Big Sales Amount :=
CALCULATE (
    [Sales Amount],
    KEEPFILTERS ( Sales[Quantity] * Sales[Net Price] > 1000 )
)
 ```
