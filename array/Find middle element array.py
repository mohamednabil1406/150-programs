# find middle element

def middle_element(arr):
    n=len(arr)
    if n%2==1:
        return arr[n//2]
    else:
        return arr[n//2-1],arr[n//2]
arr=[1,2,3,4,5]
print("the middle element",middle_element(arr))