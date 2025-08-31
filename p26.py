#def tuples_to_list_string(lst_of_tuples):
#    result = [' '.join(tup) for tup in lst_of_tuples]
#    return result

# Example usage:
#names = [('Evelyn', 'V'), ('Eva', 'Leon'),('tye','thomas'),('Theodre','Dolores')]
#print(f"Original list of tuples: {colors}")
#print(f"Converted to list of strings: {tuples_to_list_string(names)}")


integer_list = [10, 20, 30, 40, 50]
integer_tuple = (1, 2, 3, 4, 5)
string_list_from_list = list(map(str, integer_list))
string_list_from_tuple = list(map(str, integer_tuple))
print(f"Original list of integers: {integer_list}")
print(f"Converted list of strings from list: {string_list_from_list}")
print(f"Original tuple of integers: {integer_tuple}")
print(f"Converted list of strings from tuple: {string_list_from_tuple}")
