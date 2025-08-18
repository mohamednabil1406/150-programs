#  commom element in array
def common_element(a,b):
    result=[]
    used=[False]*len(b)

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j] and not used[j]:
                used[j]=True
                result.append(a[i])
                break
    return result
a = [1, 2, 1, 3, 1]
b = [3, 1, 3, 4, 1]
print(common_element(a,b))