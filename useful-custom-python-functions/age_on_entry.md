# Age On Entry

Used to calculate age on entry of a student to a programme. Can be applied to a Pandas datetime series in a dataframe.

```python
def age_on_entry(dob, entrydate):
    entrydate = datetime.strptime(entrydate, '%d/%m/%Y')
    dob = datetime.strptime(dob, '%d/%m/%Y')
    age = entrydate.year - dob.year - ((entrydate.month, entrydate.day) < (dob.month, dob.day))
    return age
```

`pdf['AgeOnEntry'] = pdf['BirthDate'].apply(lambda x: age_on_entry(dob=x, entrydate='23/09/2019'))`
