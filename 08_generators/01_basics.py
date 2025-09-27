# Generators 
# You save memory 
# You don't want the rresults immediately 
# lazy evalution 
# Yield

def serve_chai():
    yield "Cup 1 : Masala Chai"
    yield "Cup 2 : Ginger Chai"
    yield "Cup 3 : Elaichi Chai"

# this stall is keeping the refernce of whole thing
# Pauses and resume funtion o the next call exactly from that pint where it has stopped
stall = serve_chai()
for cup in stall:
    print(cup)

def get_chai_list():
    return ["Cup 1","Cup 2", "Cup3"]
# Generator funtion
def get_chai_gen():
    yield"Cup 1"
    yield"Cup 2" 
    yield"Cup3"

chai = get_chai_gen()
print(chai)
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai)) gives error