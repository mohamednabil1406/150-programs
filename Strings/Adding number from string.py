def  sum_number(s):
    total=0
    num=""
    for ch in s:
        if ch.isdigit():
            num+=ch
        else:
            if num!="":
                total+=int(num)
                num=""
    if num!="":
        total+=int(num)
    return total

text = "5ingt44t3"
print("Input :", text)
print("Output:", sum_number(text))