#highest frequency character
def highes_freqq(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    max_char=None
    max_count=0
    for ch in freq:
        if freq[ch]>max_count:
            max_char=ch
            max_count=freq[ch]
    return max_char,max_count
text = "engineering"
char, count = highes_freqq(text)
print("Input :", text)
print("Output:", char, count)