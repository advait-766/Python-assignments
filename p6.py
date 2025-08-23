maximum_of_three = lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)
print("Max is:", maximum_of_three(12, 45, 33))
