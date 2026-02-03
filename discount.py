cart_value = 3500

if cart_value >= 5000:
    discount = 20
elif cart_value >= 3000:
    discount = 10
else:
    discount = 0

print("Discount:", discount, "%")