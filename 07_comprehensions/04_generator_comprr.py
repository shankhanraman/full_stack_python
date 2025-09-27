# Generators (exression for item in iterable if condition)
# [x for x in items] makes entire list in memory 
# (x for x in items) like a stream 
daily_sales = [5,10,12,7 ,2,3,8,9,15]

total_cups = sum (sale for sale in daily_sales if sale >5)
# total_cups = [sale for sale in daily_sales if sale >5]
print(total_cups)

