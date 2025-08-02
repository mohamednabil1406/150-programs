# count the all digit  inn list
from unicodedata import digit

num=111333422445567889
digit_count=[0]*10

for digit in str(num):
    digit_count[int(digit)]+=1

print(f"Digit counts in number {num}:")
for i in range(10):
    if digit_count[i] > 0:
        print(f"Digit {i}: {digit_count[i]}")