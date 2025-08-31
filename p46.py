def is_palindrome(phrase: str) -> bool:
    cleaned = ""

    # keep only alphanumeric chars and lowercase them
    for ch in phrase:
        if ch.isalnum():          # check letter or digit (no string lib needed)
            cleaned += ch.lower() # normalize to lowercase

    # check palindrome with two pointers
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


# 🔥 Example usage
examples = [
    "Go hang a salami I'm a lasagna hog.",
    "Was it a rat I saw?",
    "Step on no pets",
    "Sit on a potato pan, Otis",
    "Lisa Bonet ate no basil",
    "Satan, oscillate my metallic sonatas",
    "I roamed under it as a tired nude Maori",
    "Rise to vote sir",
    "Dammit, I'm mad!"
]

for ex in examples:
    print(f"{ex} -> {is_palindrome(ex)}")
