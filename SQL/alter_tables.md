# Alter data in a table

`ALTER TABLE` is used to modify an existing table that has been created.

`ALTER TABLE` can be used with other statements and depending what statement is used will dictate the action.

## Add a column

The `ADD` statement can be used to add a new column to table.

```sql
ALTER TABLE person
ADD middle_name VARCHAR(20)
;
```

## Delete a column

The `DROP` statement can be used to delete a column from a table. 

```sql
ALTER TABLE person
DROP COLUMN middle_name
;
```

## Modify a column

The `ALTER COLUMN` (or `MODIFY COLUMN` if using mysql) statement can be used to change the datatype of a column.

```sql
ALTER TABLE person
MODIFY COLUMN middle_name VARCHAR(30)
;
```
