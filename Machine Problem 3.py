kilos = float(input("Enter the number of kilos bought: "))
total_price = kilos * 25.75
discount_amount = total_price * 0.15
discounted_price = total_price - discount_amount
amount_paid = float(input("Enter the amount paid: "))
change = amount_paid - total_price

print("Total price: ", total_price)
print("Discount amount: ", discount_amount)
print("Discounted price: ", discounted_price)
print("Change: ", change)
