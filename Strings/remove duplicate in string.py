#remove duplicates in string

def duplicates(s):
    result={}
    for ch in s:
        if ch not in result:
            result+=ch
    return result
s="poemppmeem"
print("after removing result:",duplicates(s))