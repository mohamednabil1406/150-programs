def reverse_sentence(s):
    word = ""
    words = []

    # Extract words manually
    for ch in s:
        if ch != " ":
            word += ch
        else:
            if word:
                words.append(word)
                word = ""
    if word:
        words.append(word)  # add last word

    # Reverse the list of words
    reversed_words = words[::-1]

    # Join them back
    return " ".join(reversed_words)


# Example
text = "Programming is fun"
print("Input :", text)
print("Output:", reverse_sentence(text))
