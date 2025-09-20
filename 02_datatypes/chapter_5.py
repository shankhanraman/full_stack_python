import sys 
from fractions import Fraction
from decimal import Decimal

# Float
ideal_temp = 95.5
current_temp = 95.49999999999999

print(f"Ideal Temp : {ideal_temp}, Current Temp : {current_temp}")
print(f"Difference : {ideal_temp - current_temp}")

print(sys.float_info)

# Complex numbers is gonna skip 