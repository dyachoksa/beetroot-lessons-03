"""
Lesson 13. Task 1.

Write a Python program to detect the number of local variables declared in a function.
"""

def number_of_local_vars(func):
    def wrapper(*args, **kwargs):
        print("Number of local variables in function {}: {}".format(
            func.__name__,
            func.__code__.co_nlocals,
        ))
        return func(*args, **kwargs)

    return wrapper


@number_of_local_vars
def print_hello():
    print("Hello")


@number_of_local_vars
def print_hello_with_var():
    msg = "Hello"
    print(msg)


@number_of_local_vars
def print_sum():
    a = 10
    b = 5
    print(a+b)


print_hello()
print_hello_with_var()
print_sum()
