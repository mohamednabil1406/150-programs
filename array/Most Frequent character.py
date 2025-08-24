#most freqent character

def most(arr):
    arr=str(arr)
    freq=[0]*10

    for ch in arr:
        freq[int(ch)]+=1
    max_count=max(freq)
    for digit in range(10):
        if freq[digit]==max_count:
            return digit
print(most(12233777)) 