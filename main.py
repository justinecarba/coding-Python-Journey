
# STUDENT GRADE ANALYZER

"""
- Ask the user how many students they want to enter.
For each student, ask for:
Student name
Grade
Store the data using a dictionary.
Calculate:
The average grade
The highest grade and student who got it
The lowest grade and student who got it
Number of students who passed (>= 75)
Number of students who failed (< 75)

"""
student = ""
students = []
grades = []

def add_student():
    num_of_students = int(input("Enter how many students: "))

    for i in range(num_of_students):
        for j in range(i):
            student_name = input(f"Enter student name {i+j}: ")
            return "Student Name:" + student_name


def calculate_average():
    math = int(input("Enter math grade: "))
    english = int(input("Enter english grade: "))
    filipino = int(input("Enter filipino grade: "))

    average = int(math + english + filipino) / 3

    return "Average  : " + average

print(calculate_average())
    

def find_highest():
    if student == "":
        print("No students recorded!!")

    else:
        print(f"Average Grade  : {grades}")

print(find_highest())

def find_lowest():
    pass

def search_student():
    pass

def display_report():
    pass







