try:
    sub1 = int(input("Enter marks obtained in Subject 1: "))
    sub2 = int(input("Enter marks obtained in Subject 2: "))
    sub3 = int(input("Enter marks obtained in Subject 3: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for the marks.")
else:
    avg_marks = (sub1 + sub2 + sub3) / 3
    print(f"Average marks: {avg_marks:.2f}")
    if avg_marks >= 90:
        print("Grade: A")
    elif avg_marks >= 80:
        print("Grade: B")
    elif avg_marks >= 70:
        print("Grade: C")
    elif avg_marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
