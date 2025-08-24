#majority  element

from collections import Counter
def majority(arr):
    n=len(arr)
    freq=Counter(arr)

    for num,count in freq.items():
        if count >n//2:
            return num
    return -1
arr = [1, 1, 2, 1, 3, 5, 1]
print(majority(arr))