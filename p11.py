quantity = int(input("Enter the quantity: "))
unit_price = 5
total_price = quantity * unit_price

# Apply discount
if quantity > 50:
    discount = 0.15  # 15% discount
elif quantity > 30:
    discount = 0.10  # 10% discount
else:
    discount = 0.0   # No discount
 
final_price = total_price * (1 - discount)
print(f"Total price before discount: Rs {total_price:.2f}")
print(f"Discount applied: {discount*100:.0f}%")
print(f"Final price to pay: Rs {final_price:.2f}")
