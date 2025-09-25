#  Dictionary = [exression for item in iterable if condition] in place of expression we have key:Value pair
tea_prices_inr= {
    "Masala Chai" : 40,
    "Elaichi Chai" : 50,
    "Spicy Chai" : 200
}

tea_prices_usd = {tea:price/80 for tea , price in tea_prices_inr.items()}
print(tea_prices_usd)

# Generator 