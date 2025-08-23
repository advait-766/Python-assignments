numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
sum_of_cubes = sum([n**3 for n in numbers])
print("The sum of cubes of the numbers is:", sum_of_cubes)
