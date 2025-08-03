num = 123456789
sum_odd = 0

for digit in str(num):
    digit = int(digit)
    if digit % 2 != 0:
        sum_odd += digit

print(sum_odd)
