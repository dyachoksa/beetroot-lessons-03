class Person:
    """The simple Person class definition"""

    number_of_persons = 0

    def __init__(self, name, age=18):
        self.name = name

        if age < 0:
            raise ValueError("Age can't be less then 0")

        self.age = age

        Person.number_of_persons += 1
        # or
        # self.number_of_persons += 1

    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")

    def celebrate_birthday(self):
        self.age = self.age + 1
        # or
        # self.age += 1

        print(f"Today' my birthday!!! Now, I'm {self.age} years old.")


print("Total persons:", Person.number_of_persons)

person1 = Person("Sergey")
print(person1.name)
person1.greet()

person2 = Person("Marry", age=20)
print(person2.name)
person2.greet()
person2.celebrate_birthday()
print(person2.age)

person3 = Person("John", age=19)
person3.greet()

print("Total persons:", Person.number_of_persons)
