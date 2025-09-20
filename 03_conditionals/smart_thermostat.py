# Building a Smart Thermostat Alert System
# You are buiding a smart thermostat alert system.
# If the device_status is "active "
#   And tmeperature > 35 -> Warn : "High temperature! Turn on AC"
#   Else "Temperature is normal"
# If device is off ->"Device is offline"

device_status = input("Enter device status (active/offline)")
if device_status =="active":
    temperature = float(input("Enter current temperature: "))
    if temperature > 35:
        print("High temperature! ")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")

