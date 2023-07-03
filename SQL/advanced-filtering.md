# Advanced filtering

Within SQL, we can use a combination of filters to produce more advanced filters. In the below example, on line 26 we use advanced filtering to remove undergraduate courses only for one college, whilst keeping their other courses.

```sql
WITH cla AS (
    SELECT DISTINCT
      fc.Student_SK,
      dc.EntityProviderCode,
      c.code as studentId,
      fc.EnrolmentStatus_SK
      FROM 
      domain.fact__commencements fc 
      INNER JOIN latest.navigate_dbo_customers c ON fc.Student_SK = c.SK
      INNER JOIN domain.dim__campus dc ON fc.Campus_SK = dc.Campus_SK
      INNER JOIN domain.dim__program dp ON fc.Program_SK = dp.Program_SK
      INNER JOIN domain.dim__teaching_period sdtp ON sdtp.BandTeachingPeriod_SK = fc.UnitBandTeachingPeriod_SK
      WHERE
      dc.SubDivisionCode IN ("UPE")
      AND AdmissionStatus_SK NOT IN ("X-Navigate Enrolment Cohort Status", "A-Navigate Enrolment Cohort Status")
      AND fc.EnrolmentStatus_SK NOT IN ("X-Navigate Registration Status")
      AND IsCommencementNotWithdrawn = 1
      AND dp.isEnglish = 0
      AND sdtp.MarketingSemester IN (202003, 202101, 202102)
      AND dc.EntityProviderCode NOT IN ("LGSC", "TPC", "THPC", "LULC") -- no LGSC and no Non-UK colleges
      AND NOT (dc.EntityProviderCode = "ARUC" AND dp.isUndergraduate = 1) -- get rid of ARUC undergraduate but keep postgraduate / any other courses
      ORDER BY
        dc.EntityProviderCode
)
```
