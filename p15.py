def calculate_factorial_for_loop(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial_result = 1
        for i in range(1, n + 1):
            factorial_result *= i 
        return factorial_result
number = 5
result = calculate_factorial_for_loop(number)
print(f"The factorial of {number} is {result}")

number_zero = 0
result_zero = calculate_factorial_for_loop(number_zero)
print(f"The factorial of {number_zero} is {result_zero}")

number_negative = -3
result_negative = calculate_factorial_for_loop(number_negative)
print(f"The factorial of {number_negative} is {result_negative}")
