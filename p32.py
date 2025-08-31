people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

print("Number of students:", len(people))
people['Lisa'] = 'Green'

print(people) 

del people['Jenny']

print(people)

sorted_people = sorted(people.items()) 

for name, color in sorted_people:

    print(f"{name}: {color}") 
