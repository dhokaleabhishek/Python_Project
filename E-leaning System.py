"""E-Learning System"""

class Person:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def display_details(self):
        print(f"The student name is :  {self.name} and its email id is : {self.email}")

class Student(Person):
    def __init__(self,student_id,course,name,email):
        self.stu_id = student_id
        self.course = course
        super().__init__(name,email)

    def enroll_course(self):
        self.display_details()
        print(f"The student id is : {self.stu_id} and currently studying the {self.course} course")

class PremiumStudent(Student):
    l1 = []
    def __init__(self,membership_level,student_id,course,name,email):
        self.mem_level = membership_level
        super().__init__(student_id,course,name,email)

    def display_premium_details(self):
        print(f"The student name is :  {self.name} and its email id is : {self.email}")
        print(f"The student id is : {self.stu_id} and currently studying the {self.course} course")
        print(f"The student premium level is : {self.mem_level}")
        dict1 = {}
        dict1 [self.stu_id] = self.name,self.email,self.course,self.mem_level
        for k,v in dict1.items():
            print(f"{k} = {v}")
        PremiumStudent.l1.append(list(dict1))
        print(PremiumStudent.l1)



p1 = PremiumStudent("3",123,"Python","Abhi","abhi@123.com")
p1.display_premium_details()
