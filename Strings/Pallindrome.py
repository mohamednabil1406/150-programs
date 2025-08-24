def is_pallindrome(s):
    l,r=0,len(s)-1
    while l<r:
        if  s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True
text="hello"
print("Palindrome" if is_pallindrome(text) else "Not Palindrome")