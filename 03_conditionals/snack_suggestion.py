# Buiding a snack system 
# A local cafe wants a program that suggests a snack.
# If a customer asks for cookies or samosa, it confirms the order
# Otherwise , it says it is not available
# Task 
# Take snack input 
# If it is "cookies" or "samosa", confirm the order
# Else , show unvailability 

snack = input("Enter your snack choice (cookies/samosa): ").strip().lower()
print(f"User said{snack}")
if snack == "cookies" or snack == "samosa":
    print(f"Great! {snack} is available. Your order is confirmed.")
else:
    print(f"Sorry, we do not have {snack} available right now.")

