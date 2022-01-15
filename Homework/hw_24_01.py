"""
Write a program that reads in a sequence of characters and prints them in reverse order, 
using your implementation of Stack.
"""
class Stack:
    def __init__(self):
        self.values = []

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.values.pop()
        except IndexError:
            raise StopIteration()

    def push(self, value: str):
        self.values.append(value)

    def pop(self):
        return self.values.pop()


def reverse_sequense(values: str):
    stack = Stack()

    for value in values:
        stack.push(value)
    
    # result = []
    # for value in stack:
    #     result.append(value)
    # return "".join(result)
    # or
    return "".join((value for value in stack))


def main():
    chars = input("Enter your sequense on characters: ")

    result = reverse_sequense(chars)

    print("Chars in reverse order:", result)


if __name__ == "__main__":
    main()
