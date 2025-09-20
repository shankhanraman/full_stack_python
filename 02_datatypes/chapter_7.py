# Tuples 
# Tuples are immutable
masala_spices = ("cardamom", "cinnamon", "clove")
# Unpacking the tuple into three variables
(spice1,spice2,spice3) = masala_spices
print(f"spice1 : {spice1}, spice2 : {spice2}, spice3 : {spice3}")

ginger_ratio , cadramom_ratio = 2,1 
print(f"ginger_ratio : {ginger_ratio}, cadramom_ratio : {cadramom_ratio}")
ginger_ratio , cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"After swap - ginger_ratio : {ginger_ratio}, cadramom_ratio : {cadramom_ratio}")


#membership 
print(f"Is ginger in masala spice ? {'ginger' in masala_spices}")
print(f"Is ginger in masala spice ? {'cardamom' in masala_spices}")
