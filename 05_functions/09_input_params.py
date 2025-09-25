# chai = "Ginger chai"
# def prepare_chai(order):
#     print("Prepareing:", order)
# prepare_chai(chai)
# print(chai)

chai = [1,2,3]


def edit_chai(cup):
    cup[1] =42

edit_chai(chai)
print(chai)


def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("Darjelling","Yes","Low")
make_chai(tea="Green",milk="No",sugar="medium")

# Args and kwargs
def special_chai(*ingredients,**extars):
    print("Ingredienst",ingredients)
    print("Extras")

special_chai("Cinnamon","Cardmom",sweetener="Honey",foam="yes")

# It is known as as default trap as list empty 
# if by mstake we execute the function the word wil be appended twice

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order)


chai_order()
chai_order()

