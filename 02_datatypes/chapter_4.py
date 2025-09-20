#Boolean datatype
is_boiling = True
string_count = 5
total_actions = string_count + is_boiling # True is treated as 1 (Upcasting)
print(f"Total actions : {total_actions}")

milk_present = 0 # no milk 
#  None -> 0 any other would convert ot 1 in boolean context
print(f"Is milk present : {bool(milk_present)}") # 0 is treated as False (Upcasting)

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can serve chai : {can_serve}")
