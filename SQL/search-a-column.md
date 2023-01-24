# Search a column

We can use wildcards to search columns in SQL, for best results temporarily parse values to lower and wrap the country in wildcards.

```sql
SELECT * 
FROM fact_countries fc 
WHERE LOWER(fc.Country) LIKE '%australia%`
```

This will search the `Country` column and return matches for countries formatted like australia, AUSTRALIA, AuStRaLiA etc.
