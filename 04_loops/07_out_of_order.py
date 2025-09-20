# Break,continue and Loop fallback
# some chai flavors are out of stock 
# You wat to skip those and stop entirely if 
# someone request a restricted flavor.
# Task:
# . Skip if flavor is " Out of stock"
# . Break if flavor is "Discontinued"

flavours = ["Ginger", "Out of Stock","Lemone", "Discontinued", "Tulsi"]

for flavour in flavours: 
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"Discontinued item found")
        break
    print(f"{flavour} item found")

print("Out of the looop")
