# Set and forzenset in python are unordered collections of unique elements.
# Sets are mutable, meaning you can add or remove elements after its creation.
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices ={"clove", "ginger", "black pepper"}

# | Union
all_spices = essential_spices | optional_spices
print(f"All spices : {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common spices : {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential : {only_in_essential}")

# Membership test 
print(f"Is 'clove' an essential spice? : {'clove' in essential_spices}")
print(f"Is 'clove' an optional spice? : {'clove' in optional_spices}")

# Frozenset is an immutable version of a set. Once created, you cannot add or remove elements from a frozenset.
frozen_essential_spices = frozenset(essential_spices)
print(f"Frozen essential spices : {frozen_essential_spices}")