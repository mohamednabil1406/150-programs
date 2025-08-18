arr = [10, 20, 30, 40]
pos = 2
arr.pop(pos-1)   # remove element at index (pos-1)
print(arr)



#without builtin


def delete_element(arr, pos):
    n = len(arr)
    for i in range(pos-1, n-1)
        arr[i] = arr[i+1]
    arr.pop()
    return arr

# Example
arr = [10, 20, 30, 40]
pos = 2
print("with out builtin ",delete_element(arr, pos))
