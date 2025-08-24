def count_word(s):
    words=s.split()
    return len(words)
text="Python is a powerful programming language"
print("string",text)
print("total no of words:",count_word(text))