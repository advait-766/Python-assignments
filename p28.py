list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
result_map_object = map(lambda x, y: x + y, list1, list2)
result_list = list(result_map_object)
print(result_list)
