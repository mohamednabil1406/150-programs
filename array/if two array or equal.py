# two array are equal

def array_equal(a,b):
    if len(a)!=len(b):
        return False
    a.sort()
    b.sort()
    for  i in range(len(a)):
        if a[i]!=b[i]:
            return False
    return True
a = [1, 2, 5, 4, 0]
b = [2, 4, 5, 0, 1]
print(array_equal(a, b))