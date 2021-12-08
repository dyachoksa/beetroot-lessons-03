"""
Write a decorator that takes a list of stop words and 
replaces them with * inside the decorated function
"""
def stop_words(words):
    def inner(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            for word in words:
                result = result.replace(word, "*")

            return result
        return wrapper
    return inner


@stop_words(["pepsi", "BMW"])
def create_slogan(name):
    return f"{name} drinks pepsi in his/her brand new BMW!"

# create_slogan = stop_words(["pepsi", "BMW"])(create_slogan)

print(create_slogan("Marry"))
