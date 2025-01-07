# Secret Santa Generator

This is a small function used to generate secret santa pairings. Ho ho ho.

```python
import random

participants = ["Adam", "Vicky", "Elle", "Billy", "Leanne", "Chelsea"]
random.shuffle(participants)

pairings = {}

for i in range(len(participants)):
    pairings[participants[i]] = participants[(i + 1) % len(participants)]

print(pairings)
```