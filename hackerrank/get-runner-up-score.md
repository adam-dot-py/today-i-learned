# Get runner up score

_Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up._

To solve, I created a function that takes the list of scores, removes duplicates and then sorts in reverse order. If the length of the list is only 1 item, then it returns the first and only item in the list, else it returns the second item in the list -- or the runner up in this case.

```python
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    def get_runner_up(a):
        unique_list = list(set(a)) # set removes duplicates from lists
        unique_list.sort(reverse=True)
        
        if len(unique_list) == 1:
            print(unique_list[0])
        else:
            print(unique_list[1])
    
    get_runner_up(arr)
```
