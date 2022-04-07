# Searching for students

This is a use case specifically for my role as MI & Data Manager. 

```sql
SELECT * FROM domain.fact__commencements
WHERE Student_SK IN (SELECT Student_SK FROM domain.dim__student WHERE studentid = student_id)
AND Campus_SK IN (SELECT Campus_SK from domain.dim__campus WHERE entityprovidercode = college)
```
