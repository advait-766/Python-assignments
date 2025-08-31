#def calculate_list_sum(numbers):
#  total_sum = sum(numbers)
#  return total_sum

# Example usage:
#my_list = [10, 25.5, 5, 80]
#result = calculate_list_sum(my_list)
#print(f"The sum of the numbers in the list is: {result}")

# Another example with an empty list
#empty_list = []
#result_empty = calculate_list_sum(empty_list)
#print(f"The sum of an empty list is: {result_empty}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = filter(lambda x: x % 2 != 0, numbers)
squared_odd_numbers = map(lambda x: x**2, odd_numbers)
sum_of_squares = sum(squared_odd_numbers)
print(f"The original list of numbers: {numbers}")
print(f"The sum of the squares of all odd numbers: {sum_of_squares}")
