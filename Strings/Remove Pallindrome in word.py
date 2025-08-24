# remove pallindrome

def remove_palindrome(s):

    words=s.split()
    result=[]
    for word in words:
        if word.lower()!=word.lower()[::-1]:
            result.append(word)
    return " ".join(result)
# Example
text = "In India Malayalam is best with dad and mom"
print("Input :", text)
print("Output:", remove_palindrome(text))