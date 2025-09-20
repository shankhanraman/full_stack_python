#String is immutable

chai_type = "ginger"
customer_name = "Priya"

print(f"Order for{customer_name} is {chai_type} chai please!")

chai_description = "Aromatic and Bold"
print(f"First word  :{chai_description[0:8]}")
print(f"Last word  :{chai_description[0:8:1]}")
print(f"Chai description :{chai_description[12:]}")
print(f"Last word :{chai_description[::-1]}") # reverse the string

# When we are using special characters
# For mandaring and chineses characters
# It looks ok in the terminal but it is not stored properly
# So better to use UTF-8 encoding
label_text ="Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label : {label_text}")
print(f"Encoded label : {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label : {decoded_label}")