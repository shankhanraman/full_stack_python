# Dictionaries in Python
chai_order = dict(type="milk", size="Large", sugar=4)
print(f"Chai order details : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Chai recipe base : {chai_recipe['base']}")
print(f"Recipe details : {chai_recipe}")

del chai_recipe["liquid"]
print(f"Updated recipe details : {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}
print(f" order details (keys) : {chai_order.keys()}")
print(f" order details (values) : {chai_order.values()}")
print(f" order details (items) : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item : {last_item}")

extra_spices = {"cinnamon" : "crushed", "ginger":"sliced"}
chai_recipe.update(extra_spices)

print(f"Updated recipe details : {chai_recipe}")

chai_size = chai_order["size"]
print(f"Chai size : {chai_size}")

# It is used .get() method to avoid KeyError
# If the value is not found, it returns None or a default value if provided
customer_note = chai_order.get("note", "No special requests")
print(f"Customer note : {customer_note}")