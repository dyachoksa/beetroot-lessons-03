class Person:
    def __init__(self, first_name, last_name, age=18):
        if age is None or age < 0:
            raise ValueError("Age should be a positive integer")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = None

    def set_email(self, email):
        self.email = email

    def send_email_message(self, email_from, subject, content):
        if self.email is None:
            print("Nothing to do. Person does not have an email...")
            return

        print("Sending email to {} from {} with subject '{}' and content:\n{}\n".format(self.email, email_from, subject, content))
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_welcome_message(self):
        return f"Hello, I'm {self.get_full_name()}. I'm {self.age} years old."


class Student(Person):
    def __init__(self, first_name, last_name, course, age=19):
        super().__init__(first_name, last_name, age)

        self.course = course
    

class Teacher(Person):
    def __init__(self, first_name, last_name, courses, salary, age=25):
        super().__init__(first_name, last_name, age)

        self.courses = courses
        self.salary = salary

    def is_teaching(self, course):
        return course in self.courses

    def print_possible_courses(self):
        print("{} can teach:".format(self.get_full_name()))
        for course in self.courses:
            print(course)


# Ramon Castro
ramon = Student("Ramon", "Castro", "Python")
ramon.set_email("ramon.castro@example.com")
print(ramon.get_welcome_message())
print(f"{ramon.first_name}'s email: {ramon.email}")
ramon.send_email_message("kim.steward@example.com", "New lesson", "You have a new lesson #12")

# Brad Freeman
brad = Student("Brad", "Freeman", "JavaScript", age=18)
print(brad.get_full_name())
print(brad.get_welcome_message())
brad.send_email_message("kim.steward@example.com", "New lesson", "You have a new lesson #12")

# Kim Steward
kim = Teacher("Kim", "Steward", ["Python", "JavaScript"], 80000, age=40)
print(kim.get_full_name())
print(kim.get_welcome_message())
print("{} is teaching PHP: {}".format(kim.first_name, kim.is_teaching("PHP")))
kim.print_possible_courses()
