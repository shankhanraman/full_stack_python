# Everything is object in python
# unique id (indentity) , type and value

sugaramount = 12
print(f"Initial sugar :{sugaramount}")

# values are change not the identity
# Variable is mutable but data is immutable
# It is just pointing to new memory location
sugaramount = 2
print(f"Second sugar :{sugaramount}")

print(f"Id of 2 :{id(2)}")
print(f"Id of 12 :{id(12)}")