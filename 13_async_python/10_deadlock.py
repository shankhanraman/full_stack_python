import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
    with lock_a:
        print("Task 1 acquired lock A")
        with lock_b:
            print("Task 1 acquired lock B")
    print("Task 1 completed")

def task2():
    with lock_b:
        print("Task 2 acquired lock B")
        with lock_a:
            print("Task 2 acquired lock A")
    print("Task 2 completed")

threading.Thread(target=task1).start()
threading.Thread(target=task2).start()

# We can use py-spy and vprof to detect deadlocks

# Pydantic does things 
# 1. Data validation
# 2. Settings management using python type annotations
# Data parsing and validation
# API developement
# config managment
# Data serilzation and deserialization