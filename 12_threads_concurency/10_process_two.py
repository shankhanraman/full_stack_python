from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crushing some members ...")
    total=0
    # for i in range(10**7):
    for i in range(10*7):
        total+=i
    print("Done ...")

# if__name_ == "__main__":
#     start = time.time()
#     processes =[Process(target=cpu_heavy) for _ in range(2)]
#     [p.start() for p in processes]
#     [p.join() for p in processes]

#     print(f"Time taken :{time.time() - start:.2f} in seconds ")