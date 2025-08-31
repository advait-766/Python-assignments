words = ["python", "functional", "programming", "is", "powerful"]

# Step 1: Use map() to calculate lengths
lengths = list(map(len, words))

# Step 2: Find the maximum length
max_len = max(lengths)

# Step 3: Use filter() to get words matching max length
longest_words = list(filter(lambda w: len(w) == max_len, words))

print("Longest word(s):", longest_words)
