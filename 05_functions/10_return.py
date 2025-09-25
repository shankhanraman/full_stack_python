def make_chai():
    return "Here is you masala chai"

return_value = make_chai()

print(return_value)

def idle_chaiwala():
    pass
print(idle_chaiwala())

def sold_cups():
    return 120

total =sold_cups()
print(total)

#  early from a from a function
def chai_status(cups_left):
    if cups_left ==0:
        return "Sorry, chai over"
    return "Chai is ready"

print(chai_status(0))
print(chai_status(5))

def chai_report():
    return 100,20  # sold remaining

sold, remaining ,_= chai_report()
print("Sold:", sold)
print("Remaining:",remaining)