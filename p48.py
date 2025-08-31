# Read input from user
text = input("Enter a string: ")

# Using lambda + map + sum
upper_count = sum(map(lambda ch: ch.isupper(), text))
lower_count = sum(map(lambda ch: ch.islower(), text))
digit_count = sum(map(lambda ch: ch.isdigit(), text))
space_count = sum(map(lambda ch: ch.isspace(), text))

# Display results
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
print("Digits:", digit_count)
print("Whitespace characters:", space_count)
