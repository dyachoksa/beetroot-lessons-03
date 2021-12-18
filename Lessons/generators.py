import sys

def numbers(max_numbers=1_000_000):
    return [f"*{n}" for n in range(1, max_numbers+1)]
print(type(numbers))

items = numbers(max_numbers=200)
print(type(items))
print(items)
print("Size of elements in memory:", sys.getsizeof(items))


def numbers_gen(max_numbers=1_000_000):
    for n in range(1, max_numbers+1):
        yield f"*{n}"
print(type(numbers_gen))

items = numbers_gen(max_numbers=200)
print(type(items))
print(items)
for item in items:
    print(item, end=" ")
print("\nSize of elements in memory:", sys.getsizeof(items))
