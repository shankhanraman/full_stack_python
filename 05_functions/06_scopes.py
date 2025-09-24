# Scopes and Name Resoultion
# Local-inside a function
# Enclosig from outer funcion fi nested 
# global - a top level script
# Built in

def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside Funcion {chai_type}")

chai_type = "lemon"
serve_chai()
print(f"Outside function: {chai_type}")

def chai_encounter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print("Inner:",chai_order)
    print_order()
    print("Outer :" ,chai_order)

chai_order = "Tulsi" #Global
chai_encounter()
print('Global :' ,chai_order)