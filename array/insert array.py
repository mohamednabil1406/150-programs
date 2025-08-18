arr=[10,20,30,40]
pos=3
ele=50

arr.insert(pos-1,ele)
print(arr)


#or without builtin
def insert_element(arr, pos, ele):
    n = len(arr)
    arr.append(0)
    for i in range(n, pos-1, -1):
        arr[i] = arr[i-1]
    arr[pos-1] = ele
    return arr

# Example
arr = [10, 20, 30, 40]
pos = 3
ele = 50
print(insert_element(arr, pos, ele))
