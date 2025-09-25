# Comprehensions are a concise way to create a lists,
# sets,
# dictionaries ,
# or generators
# in python using a single line of code 

# Why are they used in Real life?
# filter item 
# transofrm item
# create a new collection
# flatten nested structre 

# What purpose they do serve?
# cleaner code 
# Faster execution

# Types of comprehensions
# List Set Dictionay Generators 
# list [exression for item in iterable if condition]
menu = [
    "Masala Chai",
    "Iced lemon Tea",
    "Green Tea",
    "Ginger Chai"
]


# First two tea name should be same
iced_tea = [tea for tea in menu if "Iced" in tea ]
iced_tea_new = [tea for tea in menu if len(tea)>10 ]
print(iced_tea)
print(iced_tea_new)
