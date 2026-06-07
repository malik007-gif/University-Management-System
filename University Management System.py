# Class 1: Person (Parent)
# __init__: name, age
# Private: __id (auto generate)
# get_id(): id dikhao
# person_info(): name + age + id

class Person:
    count = 0
    def __init__(self,name,age):
        Person.count += 1
        self.__id = Person.count
        self.name = name
        self.age = age

    def get_id(self):
        print(self.__id)

    def person_info(self):
        return f"ID : {self.__id}\nName : {self.name}\nAge : {self.age}"


# Class 2: Student (Person se inherit)
# __init__: name, age, marks, department
# Private: __marks
# get_marks(): marks dikhao
# set_marks(): valid check (0-100)
# grade(): A/B/C/F
# is_pass(): True/False
# Static: passing_marks() → 50
# student_info(): sab print

class Student(Person):
    def __init__(self, name, age,marks,department):
        super().__init__(name,age)
        self.__marks = marks
        self.department = department

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks

        else:
            print("enter valid marks 0 to 100")


    def grade(self):
        if self.__marks >= 80:
            return "A"
        elif self.__marks >= 70:
            return "B"
        elif self.__marks >= 60:
            return "C"
        elif self.__marks >= 50:
            return "D"
        else:
            return "F"
        
    def is_pass(self):
        if self.__marks >= 50:
           return True
        else:
            return False

    @staticmethod
    def passing_marks():
        return "Passing_Marks : 50"

    def student_info(self):
        return f"Name : {self.name}\nAge : {self.age}\nDepartment : {self.department}\nMarks : {self.get_marks()}\nGrade : {self.grade()}\nStatus : {self.is_pass()}"


# Class 3: Teacher (Person se inherit)
# __init__: name, age, subject, __salary
# get_salary(): salary dikhao
# set_salary(): positive check
# give_raise(percent): salary update
# teacher_info(): sab print


class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.__salary = salary

    def get_salary(self):
        print(self.__salary)

    def set_salary(self,salary):
        if self.__salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary! Must be positive")

    def give_raise(self,percent):
        new_salary = (self.__salary * percent) / 100
        self.__salary += new_salary
        print("Salary Updated!")

    def teacher_info(self):
        return f"Name : {self.name}\nAge : {self.age}\nSubject : {self.subject}\nSalary : {self.__salary}"



# Class 4: University
# Class Attribute: uni_name = "Punjab University"
# __init__: city, students=[], teachers=[]
# add_student(student)
# add_teacher(teacher)
# show_students(): lambda sort
# show_teachers(): lambda sort
# top_students(): marks>80 Comprehension!
# department_students(dept): filter karo
# save_report(): File I/O
# summary(): poori report


class University:
    uni_name = "Punjab University"
    def __init__(self,city):
        self.city = city
        self.students = []
        self.teachers = []

    def add_student(self,student):
        self.students.append(student)

    def add_teacher(self,teacher):
        self.teachers.append(teacher)

    def show_students(self):
        self.students.sort(key=lambda s: s.name)
        return self.students

    def show_teacher(self):
        self.teachers.sort(key=lambda s: s.name)
        return self.teachers

    def top_students(self):
        topper = [s.name for s in self.students if s.get_marks() > 80]
        return topper
    
    def department(self,department):
        same_dept = []
        for s in self.students:
            if s.department == department:
                same_dept.append(s)

        return same_dept
    
    def save_report(self):
        with open("university_details.txt","w") as file:
            for s in self.students:
                file.write(s.student_info() + "\n")
            for t in self.teachers:
                file.write(t.teacher_info() + "\n")

    def summary(self):
        print("━━━━━━━━━━━━━━━━━━━━━")
        print(University.uni_name)
        print("━━━━━━━━━━━━━━━━━━━━━")
        print(Student.passing_marks())
        print("━━━━━━━━━━━━━━━━━━━━━")
        print("Students:")
        for s in self.students:
            print(s.student_info())
        print("━━━━━━━━━━━━━━━━━━━━━")
        print("Teacher:")
        for t in self.teachers:
            print(t.teacher_info())
        print("━━━━━━━━━━━━━━━━━━━━━")
        print("Top_Students :", [s.name for s in self.students if s.get_marks() > 80 ])
        print(f"Cs_Students : {[s.name for s in self.department('Computer Science')]}")
        print("━━━━━━━━━━━━━━━━━━━━━")
        self.save_report()
        print(f"Report Saved")

uni = University("Lahore")

s1 = Student("Ali",27,87,"Computer Science")
s2 = Student("Sara",39,77,"Math")
s3 = Student("Atif",32,66,"English")
s4 = Student("Zain",30,45,"Data Stracture")

uni.add_student(s1)
uni.add_student(s2)
uni.add_student(s3)
uni.add_student(s4)

t1 = Teacher("Rehman",44,"Computer Science",60000)
t2 = Teacher("Shan",48,"Math",50000)
t3 = Teacher("Hina",60,"English",70000)
t4 = Teacher("Rida",55,"Data Stracture",79000)

uni.add_teacher(t1)
uni.add_teacher(t2)
uni.add_teacher(t3)
uni.add_teacher(t4)

uni.summary()