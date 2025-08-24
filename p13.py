def simple_interest(P, R, T):
    SI = (P * R * T) / 100
    return SI
   
P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of interest: "))
T = float(input("Enter the Time (in years): "))

print(f"Simple Interest = Rs {simple_interest(P, R, T):.2f}")
