import functools
import uuid


def debug(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function '{}' with arguments {} and {}".format(func.__name__, args, kwargs))

        ret = func(*args, **kwargs)

        return ret

    return wrapper


class Person:
    # constructor/initializer of instances
    def __init__(self, name, age=18):
        if name is None or len(name) < 1:
            raise ValueError("Name can't be blank")

        self.id = uuid.uuid4()
        self.name = name
        self.age = age
    
    # string representaion/string conversion using str()
    def __str__(self):
        return self.name

    # 'Official' representation using repr()
    def __repr__(self):
        return f"<Person id={self.id} name={self.name}>"
    
    # method with decorator
    @debug
    def greet(self):
        print("Welcome, {}!".format(self.name))


class Student(Person):

    # method as attribute using 'property' decorator
    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        if type(value) is not str or len(value) < 1:
            raise ValueError("Course should be a non-empty string")

        self._course = value


class Teacher(Person):

    @classmethod
    def create(cls, name, salaries):
        obj = cls(name)

        for salary in salaries:
            obj.pay(salary)

        return obj

    def __init__(self, name, age=18):
        super().__init__(name, age=age)

        self.salaries = []
    
    def pay(self, amount):
        if amount is None or amount < 0:
            raise ValueError("Amount can't be amty or negative")
        
        self.salaries.append(amount)

    @property
    def total_paid(self):
        return sum(self.salaries)
    
    @property
    def average_salary(self):
        return sum(self.salaries) / len(self.salaries)


def main():
    kristen = Student("Kristen Palmer")
    kristen.greet()
    kristen.course = "Python for Beginners"
    print("{} is studying '{}' now.".format(kristen.name, kristen.course))

    print()

    # lesa = Teacher("Lesa Ward")
    # lesa.pay(10000)
    # lesa.pay(12000)
    # lesa.pay(11000)
    # lesa.pay(9000)
    # or
    lesa = Teacher.create("Lesa Ward", [10000, 12000, 11000, 9000])

    lesa.greet()
    print("{} salaries: {}".format(lesa.name, lesa.salaries))
    print("Average salary: ${}".format(lesa.average_salary))
    print("Total paid: ${}".format(lesa.total_paid))


if __name__ == "__main__":
    main()
