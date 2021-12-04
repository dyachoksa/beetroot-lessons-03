class Person:
    def __init__(self, name):
        # name - local to the method
        # self.name - local to the class instance
        self.name = name

    def get_name(self):
        return self.name


def print_person_name(person):
    print(person.get_name())


# global to script
person1 = Person("Mary")
print_person_name(person1)


def main():
    # local to main()
    person2 = Person("John")
    print_person_name(person2)


main()
