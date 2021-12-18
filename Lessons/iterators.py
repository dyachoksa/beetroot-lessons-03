import sys

# numbers = [1, 10, 100]
# for number in numbers:
#     print("x*x + 1000 =", number*number + 1000)

for i in range(1, 11):
    print(i, end=" ")

# similar to
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1

numbers = [n for n in range(1, 100_001)]
print(type(numbers))
print("Size of numbers:", sys.getsizeof(numbers))

numbers_it = range(1, 100_001)
print(type(numbers_it))
print("Size of numbers:", sys.getsizeof(numbers_it))

print("File reading (full file):")
with open("data.txt") as f:
    data = f.read()
print(data)

print("\nReading file (line by line):")
with open("data.txt") as f:
    for line in f:
        print(line)
