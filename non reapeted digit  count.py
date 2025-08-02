def non_repeated_digits_count(n):
    freq = [0] * 10  # To count frequency of digits

    temp = n
    if n == 0:
        print("Non-Repeated Digits: 0")
        print("Non-Repeated Count: 1")
        return

    # Count digit frequencies
    while temp > 0:
        d = temp % 10
        freq[d] += 1
        temp = temp // 10

    # Count digits that appear only once
    count = 0
    print("Non-Repeated Digits:", end=" ")
    for i in range(10):
        if freq[i] == 1:
            print(i, end=" ")
            count += 1

    print("\nNon-Repeated Count:", count)

# Example usage
num = int(input("Enter a number: "))
non_repeated_digits_count(num)
