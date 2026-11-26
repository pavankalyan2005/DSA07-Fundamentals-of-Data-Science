"""Q6: Total cost of a purchase including discount and tax."""

prices = [float(x) for x in input("Enter item prices (comma separated): ").split(",")]
quantities = [int(x) for x in input("Enter quantities (comma separated): ").split(",")]
discount_rate = float(input("Enter discount rate (%): "))
tax_rate = float(input("Enter tax rate (%): "))

if len(prices) != len(quantities):
    raise ValueError("Prices and quantities lists must have the same length")

subtotal = sum(p * q for p, q in zip(prices, quantities))
discount = subtotal * discount_rate / 100
after_discount = subtotal - discount
tax = after_discount * tax_rate / 100
total = after_discount + tax

print(f"\nSubtotal          : {subtotal:.2f}")
print(f"Discount ({discount_rate}%)  : -{discount:.2f}")
print(f"After discount    : {after_discount:.2f}")
print(f"Tax ({tax_rate}%)        : +{tax:.2f}")
print(f"TOTAL COST        : {total:.2f}")
