my_list = ['a', 'b', 'c', 'b']
try:
    index_of_b = my_list.index('b')
    my_list[index_of_b] = 'new_value'
    print(my_list)
except ValueError:
    print("'b' not found in the list.")
