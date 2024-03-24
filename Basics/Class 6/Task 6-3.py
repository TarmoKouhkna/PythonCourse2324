"""
Create a class called "Person" with attributes for name and age.
Add a method to the Person class that prints a greeting message with the person's name.
Create a subclass of Person called "Student" with an additional attribute for student ID.
Override the Person class's method in the Student subclass to include the student ID in the greeting message.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello, my name is {self.name}")


class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greeting(self):
        print(f"Hello, my name is {self.name} and my student ID is {self.student_id}")


person = Person("John", 30)
person.greeting()

student = Student("Mary", 20, 1234)
student.greeting()
