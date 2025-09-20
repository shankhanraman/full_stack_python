# Zip can combine lists 
# You are preparing an order summary with cutomer names and their total bil
# Task:
# . USe two lists : one for names and one for bills
# . Prin: "[name] paid Rs [amount]"
names = ["Anu", "Amit", "Karan", "Sonal", "Divya"]
bills = [120, 250, 90, 300, 150]

# Zip iterate over several iterables in parallel
for name, amount in zip(names, bills):
    print(f"{name} paid Rs {amount}")

