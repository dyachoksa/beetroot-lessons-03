import random


class Person:
    def __init__(self):
        self._name = None
        self._last_name = None
        self.age = None

    def __repr__(self) -> str:
        return f"<Person name={self._name} last_name={self._last_name} age={self.age}>"
    
    @classmethod
    def create(cls, name, last_name):
        obj = cls()
        obj.name = name
        obj.last_name = last_name
        obj.age = cls.get_random_age()

        return obj

    @staticmethod
    def get_random_age():
        return random.randint(0, 125)

    @property
    def full_name(self):
        "The person full name"
        return f"{self.name} {self.last_name}"

    @full_name.setter
    def full_name(self, full_name):
        if full_name is None:
            raise ValueError("Full name should not be None")

        parts = full_name.split(maxsplit=1)
        if len(parts) != 2:
            raise ValueError("Full name should be in form '<first_name> <last_name>'")
        
        self._name = parts[0]
        self._last_name = parts[1]
    
    @property
    def name(self):
        """The person name"""
        return self._name.title()
    
    @name.setter
    def name(self, name):
        if name is None or len(name) >= 15:
            raise ValueError(f"Incorrect value for name: {name}")

        self._name = name
    
    @name.deleter
    def name(self):
        del self._name

    @property
    def last_name(self):
        "The person last name"
        return self._last_name.title()

    @last_name.setter
    def last_name(self, last_name):
        if last_name is None or len(last_name) >= 15:
            raise ValueError(f"Incorrect value for last name: {last_name}")

        self._last_name = last_name
    
    # name = property(get_name, set_name, del_name, "The person name")


john = Person()
print(john)

# john.set_name("John")
# john.name = "john"
# john.last_name = "unknown"
john.full_name = "john unknown"

#print(john.get_name())
print(john.name, john.last_name)
print(john.full_name)
# full_name = f"{john.name} {john.last_name}"

marry = Person.create("Marry", "J")
print(marry)
print(marry.full_name)

print("Random age:", john.get_random_age())
