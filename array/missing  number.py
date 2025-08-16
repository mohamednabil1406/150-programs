# missing the number

def missing_number(arr):
    n=len(arr)+1
    total=n*(n+1)//2

    actual_sum=0
    for num in arr:
        actual_sum+=num
    return total-actual_sum

arr=[3,7,1,2,8,4,5]
print("missing the number",missing_number(arr))