# Upsert and merge

This is a really useful and common approach for updating source tables with new values.

## Using `SQL`

```sql
-- replace target and source with sql tables
MERGE INTO target
USING source
ON source.key = target.key
WHEN MATCHED THEN
  UPDATE SET target.lastSeen = source.timestamp
WHEN NOT MATCHED THEN
  INSERT (key, lastSeen, status) VALUES (source.key,  source.timestamp, 'active')
WHEN NOT MATCHED BY SOURCE AND target.lastSeen >= (current_date() - INTERVAL '5' DAY) THEN
  UPDATE SET target.status = 'inactive'
```

## Using `spark`

```python
(targetDF
  .merge(sourceDF, "source.key = target.key")
  .whenMatchedUpdate(
    set = {"target.lastSeen": "source.timestamp"}
  )
  .whenNotMatchedInsert(
    values = {
      "target.key": "source.key",
      "target.lastSeen": "source.timestamp",
      "target.status": "'active'"
    }
  )
  .whenNotMatchedBySourceUpdate(
    condition="target.lastSeen >= (current_date() - INTERVAL '5' DAY)",
    set = {"target.status": "'inactive'"}
  )
  .execute()
)
```

This is an example of how I did it as part of the Kafka ingestion project

```python
(targetOffsetsDeltaTable.alias("target")
    .merge(
      latestOffsetDF.alias("source"),
      "source.topic = target.topic AND source.partition = target.partition"
    )
    .whenMatchedUpdateAll()
    .whenNotMatchedInsertAll()
    .execute()
)
```