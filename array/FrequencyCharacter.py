a = [50, 20, 150, 20, 50, 10, 30, 10, 10]

# Count frequency
freq = []
for i in a:
    count = 0
    for j in a:
        if i == j:
            count += 1
    if [i, count] not in freq:   # avoid duplicates
        freq.append([i, count])

# Sort by count (descending)
for i in range(len(freq)):
    for j in range(i+1, len(freq)):
        if freq[i][1] < freq[j][1]:
            freq[i], freq[j] = freq[j], freq[i]

# Print
for num, count in freq:
    print(num, ":", count)
