def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_price = (discount_percent/100) * price
        price = price - discount_price
        print(f"Discounted Price: {round(price, 2)}")
    else:
        print(f"No discount added. Original Price: {round(price, 2)}")

price = float(input("Please enter the original price:\n"))
discount_percent = float(input("Please enter the discount percentage without the percentage sign:\n"))

calculate_discount(price, discount_percent)



