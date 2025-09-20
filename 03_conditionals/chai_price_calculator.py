# Building a chai price calculator using conditionals
# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on size.
# Task 
# Input : "small", "medium", "large"
# small : $2 , medium : $3 , large : $4
# If invalid : show "Unknown cup size"

cup = input("Enter cup size (small/medium/large): ").strip().lower()
if cup == "small":
    price = 2
    print(f"The price for a small cup of chai is ${price}.")        
elif cup == "medium":
    price = 3
    print(f"The price for a medium cup of chai is ${price}.")
elif cup == "large":
    price = 4
    print(f"The price for a large cup of chai is ${price}.")
else:
    print("Unknown cup size") 

