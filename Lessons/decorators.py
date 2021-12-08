### Simple decorator

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")

# say_hello = my_decorator(say_hello)

say_hello()


### Show execution time of some function
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")

        return result

    return wrapper


@time_it
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10_000)])

waste_some_time(10)
waste_some_time(100)
# waste_some_time(1_000)


### Decorator as validator
def validate(max_length=10, min_length=1):
    def inner(func):
        def wrapper(value, *args, **kwargs):
            if len(value) > max_length:
                raise ValueError("First argument of the '{}' function should be less then {} chars, but {} got.".format(
                    func.__name__,
                    max_length,
                    len(value),
                ))

            if len(value) < min_length:
                raise ValueError("First argument of the '{}' function should be greater then {} char(s), but {} got.".format(
                    func.__name__,
                    min_length,
                    len(value),
                ))

            return func(value, *args, **kwargs)
        return wrapper
    return inner

@validate(max_length=10, min_length=5)
def greet(name):
    print("Welcome, to the Python World, {name}!".format(name=name))

greet("Sergey")
# greet("JavaScript Master")
greet("ME")
