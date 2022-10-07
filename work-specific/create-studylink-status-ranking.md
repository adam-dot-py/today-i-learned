# Create StudyLink Status Ranks

```python
from itertools import chain
from pyspark.sql.functions import create_map, lit

studylink_status_sql = """
SELECT
    'NOTAPPLICABLE' AS StudylinkStatus_SK,
    'Not Applicable' AS StudylinkStatus
  UNION ALL
SELECT
  distinct concat(ApplicationStatus, '-sl') as StudylinkStatus_SK,
  ApplicationStatus AS StudylinkStatus
FROM
  raw.studylink_application
  """
#--load the dataframe
transaction_df = spark.sql(studylink_status_sql)

#--create the ranking dictionary. Key is StudyLink status, value is rank.
sl_statuses = [
  'Incomplete',
  'Submitted',
  'Submitted - Potential Duplicate',
  'Assessing',
  'Assessing - Pending Pre-Screening',
  'Assessing - Pending UPE Trade Sanction Check',
  'Assessing - Third Party',
  'More Information Requested',
  'Assessing - Returned from Third Party',
  'Conditional Offer',
  'Provisional Offer',
  'Cancelled',
  'Decline Indicated',
  'Declined By Applicant',
  'Deferral Indicated',
  'Withdrawn',
  'Awaiting Interview',
  'Awaiting Interview Approval',
  'Interview Decision Made',
  'Unconditional Offer',
  'Acceptance Indicated',
  'Acceptance Indicated - Pending Payment',
  'Acceptance Indicated - Payment Confirmed',
  'Acceptance Processing',
  'PCAS Assessing',
  'PCAS Assigned',
  'PCAS Ready',
  'Awaiting CAS/Visa Documentation',
  'CAS/VISA Requested from UP',
  'CAS/VISA Received from UP',
  'CAS Assigned',
  'CAS Ready',
  'Visa/EER Being Assessed',
  'Visa/EER Sent',
  'Visa sent to IND',
  'Acceptance Successful Pending Visa',
  'Visa Rejected',
  'Ready to Enrol',
  'Not Applicable'
]

rank_dict = {k:v for v, k in enumerate(sl_statuses, start=1)}

#--create a function that maps the StudyLink status to a key in the dictionary, return the value/rank
lookup_value = create_map([lit(x) for x in chain(*rank_dict.items())])

#--assign the rank to the dataframe and sort by rank. Any status not in the dictionary is assigned the length of the dictionary +1.
transaction_df = transaction_df.withColumn('StudyLinkStatusRank', lookup_value[transaction_df['StudylinkStatus']]).na.fill(len(rank_dict)+1)
transaction_df = transaction_df.orderBy('StudyLinkStatusRank')
offload_dataset_to_delta(transaction_df, "temp", "studylink_status", "overwrite", True)
```
