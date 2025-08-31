text = "Yellow Yaks like yelling and yawning and yesterday they yodeled while eating yuky yams"
vowels = "aeiouAEIOU"
consonants = [char for char in text if char.isalpha() and char not in vowels]
print(consonants)
