def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10            # Get the last digit
        rev = rev * 10 + digit    # Append the digit to reversed number
        n = n // 10               # Remove the last digit from n
    return rev

# Example
num = 143
print("Reversed number:", reverse_number(num))
