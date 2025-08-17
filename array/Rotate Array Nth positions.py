def reverse(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

# Input
arr = [1, 2, 3, 4, 5]
N = 2
length = 0


for i in arr:
    length += 1

reverse(arr, 0, N-1)

reverse(arr, N, length-1)

reverse(arr, 0, length-1)

print(arr)
