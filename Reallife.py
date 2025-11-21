print("=== Welcome to Samiullah Grocery Store ===")

items = []          # store item names
quantities = []     # store item quantities
prices = []         # store item prices

while True:
    name = input("Enter item name (or 'done' to finish): ")
    if name.lower() == "done":
        break

    qty = int(input(f"Enter quantity of {name}: "))
    price = float(input(f"Enter price of {name} (per unit): "))

    items.append(name)
    quantities.append(qty)
    prices.append(price)

print("\n=== Your Receipt ===")
subtotal = 0

for i in range(len(items)):
    cost = quantities[i] * prices[i]
    subtotal += cost
    print(f"{items[i]}  x{quantities[i]}  =  {cost} PKR")

# Apply 10% discount if total > 2000
if subtotal > 2000:
    discount = subtotal * 0.10
else:
    discount = 0

# Add 5% sales tax
tax = (subtotal - discount) * 0.05

final_total = subtotal - discount + tax

print("\nSubtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Final Total:", final_total)

print("\n=== Thank you for shopping! ===")
