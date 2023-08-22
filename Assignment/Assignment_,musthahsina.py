"""
1. Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.
"""

class Students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade


student1 = Students("Rahul",24,"9th")
print(f"Name: {student1.name}, Age: {student1.age}, Grade: {student1.grade}")


"""
2. Write a program to create a child class Teacher that will inherit the properties of Parent class Staff
"""


class Staff:
    def __init__(self,name,post,salary):
        self.name = name
        self.post = post
        self.salary = salary

class Teacher(Staff):
    def __init__(self,name,age):
        self.age = age
        super().__init__(name,"Teacher",20000)


teacher = Teacher("Maya",27)

print(f"Name: {teacher.name}, Age: {teacher.age}, Post: {teacher.post}, Salary: {teacher.salary}")



"""3.Write a Python class Square, and define two methods that return the square area and perimeter."""

class Square:
    def __init__(self,side):
        self.side = side

    def area(self):
        area = self.side*2
        print(f"Area: {area}")

    def perimeter(self):
        perimeter = 4 * self.side
        print(f"Perimeter: {perimeter}")


sq_obj = Square(5)
sq_obj.area()
sq_obj.perimeter()
    

"""4.define an account cclass with attributes ac no,ac name,balance."""

class Account:
    def __init__(self,ac_no,ac_name,balance):
        self.ac_no = ac_no
        self.ac_name = ac_name
        self.balance = balance
        
    

ac_obj = Account("00001234","James",2700)
class Account:
    def __init__(self, ac_no, ac_name, balance):
        self.ac_no = ac_no
        self.ac_name = ac_name
        self.balance = balance


account1 = Account("0001234", "Jacob", 30000)
print(f"Account Number: {account1.ac_no}, Account Name: {account1.ac_name}, Balance: {account1.balance}")



"""5.Create classes for a school management system. Have classes like Student, Teacher, and Course. Implement methods to enroll students, assign teachers, and display course details"""

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
        self.teacher = None
    
    def enroll_student(self, student):
        self.students.append(student)
    
    def assign_teacher(self, teacher):
        self.teacher = teacher
    
    def display_course_details(self):
        print("Course:", self.course_name)
        if self.teacher:
            print("Teacher:", self.teacher.name)
        else:
            print("Teacher: Not assigned yet")
        print("Students:")
        for student in self.students:
            print(student.name)


teacher1 = Teacher("Mr. Rajeev", "Mathematics")
teacher2 = Teacher("Ms. Rekha", "Accountancy")

student1 = Student("Jeeva", "A101")
student2 = Student("Gokul", "A102")

course1 = Course("Science")
course2 = Course("Commerce")

course1.assign_teacher(teacher1)
course1.enroll_student(student1)

course2.assign_teacher(teacher2)
course2.enroll_student(student2)

course1.display_course_details()
course2.display_course_details()

