# Stepping Number Check
def is_stepping(n):
    digit = [int(d) for d in str(n)]
    for i in range(len(digit) - 1):
        if abs(digit[i] - digit[i + 1]) != 1:
            return "No"
    return "Yes"

# Test
n = 12345
print(is_stepping(n))  # Output: Yes
