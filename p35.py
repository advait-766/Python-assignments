text = """Python is a high-level general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."""

letter_counts = {}
cleaned_text = text.lower()

for char in cleaned_text:
    if 'a' <= char <= 'z':  
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

for letter, count in sorted(letter_counts.items()):
    print(f"'{letter}': {count}")
