import random
import sys

numbers = [random.randint(-100, 100) for _ in range(1_000_000)]
# print(numbers)

numbers_check = [number >= 0 for number in numbers]
print(type(numbers_check))
print(sys.getsizeof(numbers_check))
all_positive = all(numbers_check)
print(all_positive)

numbers_check = (number >= 0 for number in numbers)
print(type(numbers_check))
print(sys.getsizeof(numbers_check))
all_positive = all(numbers_check)
print(all_positive)
