def process_number(number):
    if not (1000 <= number <= 9999):
        print("Please enter a valid four-digit number.")
        return
        
    num_str = str(number)
    length = len(num_str)
    
    print(f"\nProcessing number: {number}")
    for i, digit_char in enumerate(num_str):
        digit = int(digit_char)
        position = length - 1 - i
        place_value = digit * (10 ** position)
        print(f"Digit: {digit}, Face Value: {digit}, Place Value: {place_value}")
    reversed_num_str = num_str[::-1]
    print(f"Number in reverse order: {reversed_num_str}")

try:
    user_input = int(input("Enter a four-digit number: "))
    process_number(user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")

