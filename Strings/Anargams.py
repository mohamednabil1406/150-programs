from pickletools import string1


def is_anargam(str1,str2):
    return sorted(str1)==sorted(str2)
s1="listen"
s2="silent"
if is_anargam(s1,s2):
    print("is anargam")
else:
    print("not anargram")