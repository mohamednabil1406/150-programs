A = [3, 1, 2, 4]


length = 0
for _ in A:
    length += 1

total_sum = 0
i = 0


while i < length:
    j = i
    while j < length:

        min_val = A[i]
        k = i + 1
        while k <= j:
            if A[k] < min_val:
                min_val = A[k]
            k += 1
        total_sum += min_val
        j += 1
    i += 1

print(total_sum)
