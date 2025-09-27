def chai_customer():
    print("Welcome ! what chai would you like ?")
    #It waits for the the value to be entered
    order = yield 
    while True:
        print(f"Preparaing: {order} ")
        # if we remove this order yield we will get infinite result 
        order = yield

stall = chai_customer()
next(stall) # start the generator 

stall.send("Masala chai")
stall.send("Lemon  chai")