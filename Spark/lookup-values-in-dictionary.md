# Lookup Values in a Dictionary

This is great for matching items in a column to a given dictionary, similar to a `VLOOKUP()` in Excel.

```python
from itertools import chain
from pyspark.sql.functions import create_map, lit

#--load the dataframe
transaction_df = spark.sql(studylink_status_sql)

#--create the ranking dictionary. Key is StudyLink status, value is rank.
rank_dict = {
  'Submitted' : 1,
  'Submitted - Potential Duplicate' : 2,
  'Assessing' : 3,
  'Assessing - Pending Pre-Screening' : 4,
  'Assessing - Pending UPE Trade Sanction Check' : 5,
  'Assessing - Third Party' : 6,
  'More Information Requested' : 7,
  'Assessing - Returned from Third Party' : 8,
  'Conditional Offer' : 9,
  'Provisional Offer' : 10,
  'Cancelled' : 11,
  'Decline Indicated' : 12,
  'Declined By Applicant' : 13,
  'Deferral Indicated' : 14,
  'Withdrawn' : 15,
  'Awaiting Interview' : 16,
  'Awaiting Interview Approval' : 17,
  'Unconditional Offer' : 18,
  'Acceptance Indicated' : 19,
  'Acceptance Indicated - Pending Payment' : 20,
  'Acceptance Processing' : 21,
  'PCAS Assessing' : 22,
  'PCAS Assigned' : 23,
  'PCAS Ready' : 24,
  'Awaiting CAS/Visa Documentation' : 25,
  'CAS/VISA Requested from UP' : 26,
  'CAS/VISA Received from UP' : 27,
  'CAS Assigned' : 28,
  'CAS Ready' : 29,
  'Ready to Enrol' : 30,
  'Not Applicable' : 31}

#--create a function that maps the StudyLink status to a key in the dictionary, return the value/rank
lookup_value = create_map([lit(x) for x in chain(*rank_dict.items())])

#--assign the rank to the dataframe and sort by rank. Any status not in the dictionary is assigned the length of the dictionary +1.
transaction_df = transaction_df.withColumn('StudyLinkStatusRank', lookup_value[transaction_df['StudylinkStatus']]).na.fill(len(rank_dict)+1)
transaction_df = transaction_df.orderBy('StudyLinkStatusRank')
```
