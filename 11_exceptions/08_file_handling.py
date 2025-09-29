# file = open("order.txt","w") file__enter__() dunder is called
# try:
#     file.write("Masala Chai - 2 cups")
# finally:
#     file.close() file__exit__() dunder is called 

# Modern way instead of try catch
with open("order.txt","w") as file:
    file.write("ginger tea - 4 cups")
