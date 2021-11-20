name = "The functions.py script"


def greet():
    name = "Beetroot"
    print(name)
    print("Hello, Python World!")


greet()
print("")


def calculate_total(amount, discount):
    return amount - (amount*discount)


total = calculate_total(99.99, 0.1)
print("Total for amount 99.99 and discount 10%:", total)
print("")


def greet_person(name, age=None, has_car=False):
    print("Hello, {}".format(name))

    if age is not None:
        print("You are {} years old.".format(age))


greet_person("Sergey", 18)
greet_person("Sara")
greet_person("John", age=21)
print("")


def print_user(user):
    print(
        "Name: {} {} / Email: {}".format(user["first_name"], user["last_name"], user["email"]))


marjorie = {
    "first_name": "Marjorie",
    "last_name": "Dunn",
    "email": "marjorie.dunn@example.com",
    "age": 21
}
print_user(marjorie)
print_user({"first_name": "F", "last_name": "L", "email": "user@example.com"})
print("")

print(name)
