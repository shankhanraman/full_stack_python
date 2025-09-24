# You sell differnet chaii sizes 
# Instead of writing formulas everywhere , create a function 
#  Task:
# .Write calculate_bills(cups, price_per_cup)
# .Return total bill
# .Use this function for multiple orders 
def calulcalate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calulcalate_bill(3,15)
print(my_bill)

print("Order for table 2:",calulcalate_bill(2,50))