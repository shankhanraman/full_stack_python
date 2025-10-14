import threading
import time
def take_orders():
    for i in range(1,4):
        print(f"Taking orders for #{i}")
        time.sleep(2)
    
def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)

# create threads 
order_threads =threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

order_threads.start()
brew_thread.start()

# wait for both to finish
order_threads.join()
brew_thread.join()

print(f"All orders taken and chai brewed")
