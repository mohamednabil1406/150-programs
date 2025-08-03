# is pallindrome number
from unicodedata import digit


def is_pallindrome(n):
    o=n
    r=0
    while n>0:
        digit=n%10
        r=r*10+digit
        n//=10
    return o==r

n=121
print(is_pallindrome(n))