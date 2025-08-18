def two_sum(arr,target):
    n=len(arr)
    for i in range(n):
        for  j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return [i,j]
    return []
arr = [0, -1, 2, -3, 1]
target = -2
print(two_sum(arr, target))