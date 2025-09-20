# walrus operator 
# value =13
# remainder = value % 3
# if remainder:
#     print(f"Not divisble , remainder is {remainder}")
# Python avoids this confusion by forbidding assignments inside expressions.
# throws an error. Guido van Rossum (Python’s creator) chose this rule so that:
# Code is more readable.
# You don’t accidentally confuse assignment with comparison.
# It forces you to be explicit: assignment (=) must be separate from condition checks.
value =13 

if remainder := value % 5:
    print(f"Not divisible ,remainder is {remainder}")

available_sizes=["small","medium","large"]

if(requested_size:= input("Enter your chai cup size")) in available_sizes:
    print(f"Serving {requested_size}  chai")
else:
    print(f"Size is unavailable -{requested_size}")

flavours = ["masale","ginger","lemon","mint"]
print("Available flavours:",flavours)

while(flavour:=input("Choose your flavor:")) not in flavours:
    print(f"Sorry , {flavour} is not available")

print(f"You choose {flavour} chai")


