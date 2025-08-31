def find_longest_item(iterable):
  if not iterable:
    return None
  return max(iterable, key=len)
words = ["ios", "mario", "nioh", "cyberpunk", "elden ring"]
longest_word = find_longest_item(words)
print(f"The longest word is: {longest_word}")
nested_lists = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
longest_list = find_longest_item(nested_lists)
print(f"The longest list is: {longest_list}")
empty_list = []
result_empty = find_longest_item(empty_list)
print(f"Longest item in an empty list: {result_empty}")
