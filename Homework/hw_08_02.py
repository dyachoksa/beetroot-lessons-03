a = input('A: ')
b = input('B: ')

try:
    a = int(a)
    x = a**2

    b = int(b)
    print(x / b)
except ValueError:
    print("Only integers are allowed")
except ZeroDivisionError:
    print("You can't divide by zero")

# except:
#     if type(a) is not int and type(b) is not int:
#         print("Only integers are allowed")

#     if b == 0:
#         print("You can't divide by zero")
