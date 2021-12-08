"""
Write a function called `choose_func` which takes a list of nums and 2 callback functions. 
If all nums inside the list are positive, execute the first function on that list and return 
the result of it. Otherwise, return the result of the second one.
"""
def choose_func(numbers, func1, func2):
    # simplest solution
    # is_all_positive = True
    # for number in numbers:
    #     if number < 0:
    #         is_all_positive = False
    #         break

    # using min()
    # is_all_positive = min(numbers) >= 0

    # using all()
    is_all_positive = all([number >= 0 for number in numbers])

    if is_all_positive:
        return func1(numbers)
    
    return func2(numbers)


def square_nums(numbers):
    return [number ** 2 for number in numbers]


def remove_negatives(numbers):
    return [number for number in numbers if number > 0]


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

# assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
# assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))
