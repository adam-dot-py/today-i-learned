# Store git credentials in `git credential manager`

If using the `git credential manager`, you can cache and store access tokens for repos securely, for a period of specified time. You change the specified time like so:

```python
# Cache for 1 hour
git config --global credential.helper "cache --timeout=3600"

# Cache for 1 day
git config --global credential.helper "cache --timeout=86400"

# Cache for 1 week
git config --global credential.helper "cache --timeout=604800"
```