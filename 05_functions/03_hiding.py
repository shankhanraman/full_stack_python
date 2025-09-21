# # You are building a simple app that register users .
# You wan to t oseparate concerns : geting input , validating it and saving it.
# Task:
# .Write register_user() that calls :
# .get_input()
# .validate_input()
# .save_to_db()

def get_input():
    print("Getting user input")

def validate_input():
    print("Validating the user info")

def save_to_db():
    print("saving to database")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registeration is complete")

register_user()

