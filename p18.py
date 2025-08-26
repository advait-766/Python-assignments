vowels = ['a', 'e', 'i', 'o', 'i', 'u']
element_to_find = 'e'

try:
    index_of_e = vowels.index(element_to_find)
    print(f"The index of '{element_to_find}' is: {index_of_e}")
except ValueError:
    print(f"'{element_to_find}' is not found in the list.")
