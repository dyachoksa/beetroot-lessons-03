numbers = []
filtered_numbers = []

i = 1
while i <= 100:
    numbers.append(i)
    i += 1

print("Original numbers:", numbers)

i = 0
while i < len(numbers):
    current_number = numbers[i]

    if current_number % 7 == 0 and current_number % 5 != 0:
        filtered_numbers.append(current_number)
    i += 1

print("Filtered numbers:", filtered_numbers)
