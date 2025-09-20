# Delivery fees waiver system
# You run an oniline tea store.
# If the order amoun is more than Rs 300 , delivery is free;
# otherwise it costs Rs 30.

# Task:
# .Input: order_amount
# .use ternary operator to decide delivery fee 

order_amount = int(input("Enter order amount."))

print(f"Order amount is {order_amount}")

deliver_fee = 0 if order_amount > 300 else 30

print(f"Delivery fee is {deliver_fee}")


