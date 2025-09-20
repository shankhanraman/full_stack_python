# Basic of list in Python
ingredients = ["water","milk","black tea"]
ingredients.append("sugar")
print(f"Ingredients : {ingredients}")
ingredients.remove("water")
print(f"Ingredients are : {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water","milk"]

chai_ingredients.extend(spice_options)
print(f"Chai ingredients are : {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"Chai ingredients are : {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Last added ingredient : {last_added}")
print(f"Chai ingredients are : {chai_ingredients}")

chai_ingredients.reverse()
print(f"Chai ingredients are : {chai_ingredients}")

chai_ingredients.sort()
print(f"Chai ingredients are : {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum Sugar levels : {max(sugar_levels)}")
print(f"Minimum Sugar levels : {min(sugar_levels)}")

# Operator Overloading and bytearray in Python

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

# Operator Overloading
full_liquid_mix = base_liquid + extra_flavor
print(f"Full liquid mix : {full_liquid_mix}")

strong_brew = ["black tea","water"] * 3
print(f"String brew : {strong_brew}")

from operator import itemgetter
# "CINNAMON" 
# O <B<256 
raw_spice_data = bytearray(b"CINNAMON")
print(f"Bytes : {raw_spice_data}")

raw_spice_data=raw_spice_data.replace(b"CINNA",b"CARD")
print(f"Changed Bytes : {raw_spice_data}")