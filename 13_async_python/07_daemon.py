import threading
import time

def monitor_tea_temp():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(4)

threading.Thread(target=monitor_tea_temp, daemon=True).start()

print("Main program is done...")
