import random
import time
from turtle import right


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
def bubble_sort(elements):
    n_elements = len(elements)

    for steps in range(n_elements-1, 0, -1):
        for i in range(steps):
            if elements[i] > elements[i+1]:
                # temp = elements[i]
                # elements[i] = elements[i+1]
                # elements[i+1] = temp
                # or
                elements[i], elements[i+1] = elements[i+1], elements[i]


@time_it
def merge_sort(elements):
    def inner_sort(values):
        if len(values) <= 1:
            return values

        m_index = len(values) // 2

        left = values[:m_index]
        right = values[m_index:]

        left = inner_sort(left)
        right = inner_sort(right)

        return merge(left, right)

    return inner_sort(elements)


def merge(left, right):
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    
    if len(left) == 0:
        result += right
    else:
        result += left
    
    return result


def main():
    print("Sorting 100 numbers:")
    numbers = [random.randint(1, 1_000_000) for _ in range(100)]
    bubble_sort(numbers)
    numbers = [random.randint(1, 1_000_000) for _ in range(100)]
    merge_sort(numbers)

    print("Sorting 1000 numbers:")
    numbers = [random.randint(1, 1_000_000) for _ in range(1_000)]
    bubble_sort(numbers)
    numbers = [random.randint(1, 1_000_000) for _ in range(1_000)]
    merge_sort(numbers)

    print("Sorting 10000 numbers:")
    numbers = [random.randint(1, 1_000_000) for _ in range(10_000)]
    bubble_sort(numbers)
    numbers = [random.randint(1, 1_000_000) for _ in range(10_000)]
    merge_sort(numbers)

    print("Sorting 100000 numbers:")
    numbers = [random.randint(1, 1_000_000) for _ in range(100_000)]
    merge_sort(numbers)


if __name__ == "__main__":
    main()
