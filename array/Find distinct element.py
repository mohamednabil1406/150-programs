def findDistinct(arr, n):
    distinct = []

    for i in range(n):
        # check if arr[i] appeared before
        flag = False
        for j in range(i):
            if arr[i] == arr[j]:
                flag = True
                break
        if not flag:
            distinct.append(arr[i])

    print(distinct)


# Example
arr = [12, 10, 9, 45, 2, 10, 10, 45]
n = len(arr)
findDistinct(arr, n)
