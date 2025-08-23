try:
    num_calls = int(input("Enter the number of calls: "))
    if num_calls < 0:
        print("Number of calls cannot be negative. Please enter a valid number.")
    else:
        bill = 0.0
        if num_calls <= 100:
            bill = 200.0
        elif num_calls <= 150:
            bill = 200.0 + (num_calls - 100) * 0.60
        elif num_calls <= 200:
            bill = 200.0 + (50 * 0.60) + (num_calls - 150) * 0.50
        else:
            bill = 200.0 + (50 * 0.60) + (50 * 0.50) + (num_calls - 200) * 0.40
        print(f"The monthly telephone bill is: Rs. {bill:.2f}")
except ValueError:
    print("Invalid input. Please enter a whole number.")
