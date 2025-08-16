#second largest

def second_large(arr):
    first=second=-99999999

    for num in arr:
        if num>first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num

    if second==-99999999:
            return None
    return second
arr=[12,35,1,10,34,1]#exmaple
print("the second laregst",second_large(arr))