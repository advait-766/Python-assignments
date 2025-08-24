a = float(input("Enter farenheit F temperature to convert into celcius : "))
b = float(input("Enter Celcius C temperature to convert into Farenheit : "))
ftoc = lambda a: (a-32)*5/9
ctof = lambda b: (b*9/5)+32
print(f"Farenheit to celcius : {ftoc(a)}")
print(f"Celcius to farenheit : {ctof(b)}")
