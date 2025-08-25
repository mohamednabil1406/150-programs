def count_all(s):
    vowels = "aeiouAEIOU"
    v_count = d_count = s_count = c_count = 0

    for ch in s:
        if ch.isalpha():   # alphabet check
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
        elif ch.isdigit():
            d_count += 1
        else:
            s_count += 1

    return v_count, c_count, d_count, s_count

# Example
text = "Hello World! 123 @Python"
v, c, d, sp = count_all(text)
print("Input String:", text)
print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special Characters:", sp)
