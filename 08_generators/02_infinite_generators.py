def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count+=1

refill = infinite_chai()

for __ in range(5):
    print(next(refill))

for __ in range(6):
    print(next(user2))