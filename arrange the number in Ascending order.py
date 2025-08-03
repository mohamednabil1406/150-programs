def is_ascending(n):
    digits = [int(d) for d in str(n)]
    for i in range(len(digits) - 1):
        if digits[i] >= digits[i + 1]:
            return "No"
    return "Yes"

# Test cases
print(is_ascending(4567))  # Output: Yes
print(is_ascending(4576))  # Output: No
