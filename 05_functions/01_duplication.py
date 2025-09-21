# # Functions - Reducing Duplication and Splitting Complex Tasks
# You managing a busy tea stall
# You receive many orders and want to print ech customer's name along with the type of chai they ordered 
# Task:
# . Write a function print_order(name,chai_type)
# . Call it multiple times for different customers 

# Here it is parameter if we are passing a variable 
def print_order(name,chai_type):
    print(f"{name} ordered {chai_type} chai")
# Here it is called argument if we pass variable 
print_order("Aman","Masala")
print_order("Hitesh","Ginger")
print_order("jia","Tulsi")
