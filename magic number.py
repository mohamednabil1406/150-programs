def is_magic_number(num):
    while num > 9:
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        num = sum_digits
    return num == 1

# Example
number = 50113
if is_magic_number(number):
    print(f"{number} is a Magic Number")
else:
    print(f"{number} is NOT a Magic Number")
