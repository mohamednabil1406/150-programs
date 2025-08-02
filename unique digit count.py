def unique_digits_info(n):
    digit_seen = [0] * 10  # Track digits 0-9
    unique_digits = []     # Store unique digits
    count = 0

    if n == 0:
        print("Unique Digits: 0")
        print("Unique Digits Count: 1")
        return

    while n > 0:
        digit = n % 10
        if digit_seen[digit] == 0:
            digit_seen[digit] = 1
            unique_digits.append(digit)
            count += 1
        n = n // 10

    print("Unique Digits:", end=" ")
    for d in unique_digits:
        print(d, end=" ")
    print("\nUnique Digits Count:", count)

# Example usage
num = int(input("Enter a number: "))
unique_digits_info(num)
