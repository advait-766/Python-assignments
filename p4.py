try:
	print("Enter three integer numbers for average : ")
	a = int(input(" "))
	b = int(input(" "))
	c = int(input(" "))
except ValueError:
	print("Enter valid integers")
average = lambda a,b,c: a+b+c/3
print(f"Average of entered numbers is : {average(a,b,c)}")
