ch = input("Enter a character: ")
if len(ch) != 1 or not ch.isalpha():
    print("Invalid input! Please enter a single alphabet.")
else:
    ch = ch.lower()

    if ch in ['a', 'e', 'i', 'o', 'u']:
        print(f"{ch} is a Vowel")
    else:
        print(f"{ch} is a Consonant")
