#search specif arr

def  search_specific(arr):
    search=10

    result=[]
    count=1
    for  i in arr:
        if i==search:
            result.append(i)
            result.append(count)
            count+=1
        else:
            result.append(i)
    return result
arr=[10,20,10,30,14,14,60,10]
print("alter array is",search_specific(arr))

