# Using the LAG clause

SQL `LAG()` is a window function that provides access to a row at a specified physical offset which comes before the current row.

In other words, by using the `LAG()` function, from the current row, you can access data of the previous row, or from the second row before the current row, or from the third row before current row, and so on.

## Example

### Create the `basic_pays` table

```sql
CREATE TABLE basic_pays (
employee_id int,
fiscal_year INT,
salary DECIMAL (10 , 2 ),
PRIMARY KEY (employee_id, fiscal_year)
);
```

### Add some data

```sql
INSERT INTO basic_pays(employee_id, fiscal_year, salary) VALUES(100, 2017, 24000);
INSERT INTO basic_pays(employee_id, fiscal_year, salary) VALUES (100, 2018, 18190)
INSERT INTO basic_pays(employee_id, fiscal_year, salary) VALUES (100, 2019, 25000);
```

### Use the `LAG` clause

```sql
SELECT 
employee_id, 
fiscal_year, 
salary,
LAG(salary) OVER (
    PARTITION BY employee_id 
    ORDER BY fiscal_year) previous_salary
FROM
basic_pays;
```

![basic_pays_output](/graph_examples/basic_pays_output.png)

- First, the `PARTITION BY` clause divided the result set into groups by `employee ID`.
- Second, for each group, the `ORDER BY` clause sorted the rows by `fiscal_year` in ascending order.
- Third, `LAG()` function applied to the row of each group independently. The first row in each group was `NULL` because there was no previous year’s salary. The second and third row gots the salary from the first and second row and populated them into the `previous_salary` column.
