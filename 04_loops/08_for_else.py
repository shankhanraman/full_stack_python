staff = [("amit",16),("Zara",17),("Raj",15)]

for name,age in staff:
    if age>=18:
        print(f"{name} is eligible to manage the staff")
        break
# Else block wil only only run when loop does not break
# Fallback logic or not found 
else:
    print(f"No one is eligibel to manage the staff")