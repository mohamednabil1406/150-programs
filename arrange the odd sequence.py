def process_number(n):
    odd_digits = []
    even_digits = []
    sum_of_odds = 0

    for ch in str(n):
        digit = int(ch)
        if digit % 2 != 0:  # odd
            odd_digits.append(str(digit))
            sum_of_odds += digit
        else:  # even
            even_digits.append(str(digit))

    rearranged_number = ''.join(odd_digits + even_digits)
    print("Sum of odd digits:", sum_of_odds)
    print("Rearranged number:", rearranged_number)

# Test
n = 361589
process_number(n)
