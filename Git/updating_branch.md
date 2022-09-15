# Updating branches

We can do this by doing a `rebase`:

```git
git fetch
git rebase master
```

You can also perform a `merge`:

```git
git checkout <branch>
git merge master
```
