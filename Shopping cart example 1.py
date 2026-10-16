#Shopping cart

item = input("What are you buying? ")
price: float|int = float(input("Enter the price: "))
quantity = int(input("How many of the item: "))
total = price * quantity

print(f"You have bought {quantity} x {item}")
(print(f"Your total is ${round(total, 2)}"))
