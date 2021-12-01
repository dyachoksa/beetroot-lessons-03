numbers = [10, 100, 1000]

print("Start work")

try:
    print("I'm try block")
    print("3:", numbers[2])
    print("4:", numbers[3])
except IndexError:
    print("You are trying to access non-existing element in the list")
    print("I'm except block")
finally:
    print("I'm finally block")

print("Finish work")
