# Introducing while loop in Python
# You want to simulate tea heating 
# It starts at 40 degrees C and boils at 100 degrees C
# Task: 
# . Use a while loop
# Increase temperature by 15 until it reaches 100
# Print each temperature step

temperature = 40
while temperature < 100:
    print(f"Current temperature : {temperature}C")
    temperature += 15
print("Tea has boiled! Please turn off the kettle.")

