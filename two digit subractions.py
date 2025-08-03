# Two-digit subtraction form

def is_subtractions(n):
    digit = []
    for i in str(n):
        digit.append(int(i))

    while len(digit) > 2:
        new_digit = []
        for j in range(len(digit) - 1):
            diff = abs(digit[j] - digit[j + 1])  # Use j instead of i
            new_digit.append(diff)
        digit = new_digit

    result = digit[0] * 10 + digit[1]
    return result

# Test
n = 6928
print(is_subtractions(n))  # Output: 41
