import datetime
import pprint


def debug_info(value):
    pprint.pprint(value)


def income_table(items, symbol="$", prepend=False):
    for item in items:
        if prepend:
            print(f"{symbol}{item}")
        else:
            print(f"{item}{symbol}")


def print_numbers():
    numbers = [x for x in range(1, 101)]

    the_index_of_the_current_element = 0
    while the_index_of_the_current_element < len(numbers):
        if numbers[the_index_of_the_current_element] % 5 == 0:
            print(numbers[the_index_of_the_current_element], end=" ")

        the_index_of_the_current_element = the_index_of_the_current_element + 1


def calculate_total_income(items, tax=0):
    total = 0

    # tax in form of '12%'
    if tax > 1:
        tax = round(tax / 100, 4)  # to have 0.1200 and not 0.120000001

    for item in items:
        net_income = item - (item*tax)
        total += net_income

    return total


def main():
    # string
    name = "Willie"

    # numbers
    age = 23
    tax = 8.5  # 8.5% of tax

    # booleans - True/False
    is_student = False

    # special value None
    nothing = None

    # sequenses - lists, tuples and sets
    # list
    income = [12000, 12000, 11000, 12500, 10850, 9000]
    # tuple
    # one element (10,)
    # two elsements (10, 100)
    # more (10, 100, 1000)
    full_name = ("Willie", "Watkins")
    # set
    numbers = {10, 10, 100, 100, 100}  # will store only {10, 100, 1000}

    # dictionary - dict
    user_info = {
        "first_name": name,
        "last_name": "Watkins",
        "email": "willie.watkins@example.com",
        "age": age,
        "last_6_months_income": income,
    }

    debug_info(user_info)
    print("")

    # without optional argument
    # income_table(income)

    # with optional argument
    # income_table(income, symbol=" USD")

    income_table(income, prepend=True)

    total_income = calculate_total_income(
        user_info["last_6_months_income"], tax=tax)

    print("{name} {last_name}, {age} years old. Email: {email}".format(
        name=full_name[0],
        last_name=full_name[1],
        age=age,
        email=user_info['email']
    ))
    print(f"Total net income for the last 6 months: ${total_income}")


# a < 10
# a > 100
# age == 18
# x > 0 and x < 10
# name == "John" or name == "Marry"
# 12000 in income
# 8000 not in income
if __name__ == "__main__":
    print("Hello! Today is {}".format(datetime.datetime.now()))

    main()

    print("")
    print_numbers()
