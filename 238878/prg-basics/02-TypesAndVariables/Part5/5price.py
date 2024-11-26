price = input("Enter price: ")
discount = input("Enter discount in %: ")
price = float(price)
discount = float(discount)
reduction = price * (discount / 100)
price_w_disc = price - reduction
print(f"Price: {price:.2f}\nDiscount: {discount:.0f}%\nPrice with discount: {price_w_disc:.2f}\nReduction: {reduction:.2f}")