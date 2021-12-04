def add(x, y):
    return x + y

def sub(x, y):
    return x - y


def operation(op, x, y):
    return op(x, y)


print("2 + 3 =", operation(add, 2, 3))
print("3 - 2 =", operation(sub, 3, 2))


def div_by_5(value):
    return value % 5 == 0


def div_by_10(value):
    return value % 10 == 0


def is_positive(value):
    return value > 0


numbers = [x for x in range(-50, 51)]
print(list(filter(div_by_5, numbers)))
print(list(filter(div_by_10, numbers)))
print(list(filter(is_positive, numbers)))

def apply(op, elements):
    result = []
    for el in elements:
        result.append(op(el))
    
    return result


def add_10(value):
    return value + 10

def sub_5(value):
    return value - 5

def mul_by_2(value):
    return value * 2


numbers = [x for x in range(1, 11)]
print(apply(add_10, numbers))


def apply_list(operations, elements):
    result = []

    for el in elements:

        inner_result = el
        for op in operations:
            inner_result = op(inner_result)
        
        result.append(inner_result)

    return result


numbers = [x for x in range(1, 11)]
print(numbers)
print(apply_list([add_10, sub_5, mul_by_2], numbers))


def make_add(x):
    def inner(value):
        return value + x

    return inner

numbers = [x for x in range(1, 11)]
print(numbers)
print(apply_list([make_add(10), make_add(5), make_add(2)], numbers))
