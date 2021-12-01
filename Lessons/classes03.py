class Animal:
    def __init__(self, age=None):
        self.age = age
        self.name = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Animal name={self.name} age={self.age}>"

    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False
        
        return self.name == other.name and self.age == other.age
    
    def __len__(self):
        return self.age

    def __add__(self, other):
        if type(other) is not int:
            raise ValueError("Can add only integers to the Animal instances")

        self.age += other
        return self

    def __int__(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def say(self):
        print("Animals can't talk...")


class Cat(Animal):
    def say(self):
        print("meow meow")


class Dog(Animal):
    def say(self):
        print("woof woof")

cat = Cat(age=3)
cat.set_name("Kitty")

print("Cat instance:", repr(cat))
print("Cat's name:", cat)
# or
# print("Cat's name:", str(cat))

cat1 = Cat(age=2)
cat1.set_name("Kitty")
print("Cat1 instance:", repr(cat1))

cat1 += 1
print("After cat1 += 1:", repr(cat1))

print("cat == cat1:", cat == cat1)

print("Len of cat:", len(cat))
print("Age:", int(cat))

# some_animal = Animal()
# some_animal.say()

# dog1 = Dog(age=5)

# print("Age of cat:", cat1.get_age())

# cat1.say()
# dog1.say()
