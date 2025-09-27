from functools import wraps
def my_decorator(func):
    @wraps(func) # it preserves metada from changing``
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class fom chaicode")

greet()
print(greet.__name__)