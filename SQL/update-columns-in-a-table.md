# Updating columns in a table

Below is considered safe best practice for updating the data type of a column in SQL but the concept can also be applied to other update actions if required.

```sql
-- 1. Add a new column with TIMESTAMP type
ALTER TABLE edp.raw.studylink_application ADD COLUMNS (submissionDate_ts TIMESTAMP);

-- 2. Populate the new column by casting
UPDATE edp.raw.studylink_application
SET submissionDate_ts = CAST(submissionDate AS TIMESTAMP);

-- 3. Drop the old column and rename the new one
ALTER TABLE edp.raw.studylink_application SET TBLPROPERTIES ('delta.columnMapping.mode' = 'name');
ALTER TABLE edp.raw.studylink_application DROP COLUMN submissionDate;
ALTER TABLE edp.raw.studylink_application RENAME COLUMN submissionDate_ts TO submissionDate;

-- 4. Check
select submissionDate from edp.raw.studylink_application order by submissionDate desc limit 10;
```