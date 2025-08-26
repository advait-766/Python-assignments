def find_largest_number():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")

    if not numbers:
        print("No numbers were entered.")
        return

    largest = numbers[0]  

    for number in numbers:
        if number > largest:
            largest = number 

    print(f"The largest number in the list is: {largest}")
find_largest_number()
