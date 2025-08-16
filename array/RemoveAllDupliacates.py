#remove all dupliactes


def remove_duplicates(arr):
    res=[]
    for num in arr:
        if num  not in res:
            res.append(num)
    return res
arr=[1,2,3,3,4,4,5]
print("after removing the dupliactes",remove_duplicates(arr))