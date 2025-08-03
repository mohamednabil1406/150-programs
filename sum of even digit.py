num = 123456789
sum_even = 0

for digit in str(num):
    digit = int(digit)
    if digit % 2 == 0:
        print(digit,end=" ")
        sum_even += digit

print(sum_even)
