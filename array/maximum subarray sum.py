arr = [2, 3, -8, 7, -1, 2, 3]

max_ending_here = arr[0]
max_so_far = arr[0]

i = 1
while i < len(arr):

    if max_ending_here + arr[i] > arr[i]:
        max_ending_here = max_ending_here + arr[i]
    else:
        max_ending_here = arr[i]

    if max_ending_here > max_so_far:
        max_so_far = max_ending_here

    i += 1

print(max_so_far)
