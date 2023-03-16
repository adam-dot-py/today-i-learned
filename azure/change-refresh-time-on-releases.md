# Change refresh times on releases

This can be done by going to the Pipeline, then to Tasks and amending the `schedule_body` `json` field.

```json
{ "value": { "days": [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ], "times": [ "19:00","21:00", "23:00" ], "localTimeZoneId": "UTC" } }
```
