class Chai:
    temperature = "hot"
    strength ="Strong"

cutting = Chai()
print(cutting.temperature)

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing " , cutting.temperature)
print("Cup size is  " , cutting.cup)
print("Directly look into class",Chai.temperature)

# If we have nothing to fallback it woukd show error 
#  If we have properties defined in class itself it would refer to that after deleting automatically
# This is called attribitue shadowing
del cutting.temperature
del cutting.cup
print(cutting.temperature)
print(cutting.cup)