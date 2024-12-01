"""E-Learning System"""


class Student:
    def __init__(self,student_id,course,name,email):
        self.stu_id = input("Enter student Roll No. : = ")
        while True:
            if self.stu_id.isdigit():
                break
            else:
                print("Enter Correct Roll No.")
                self.stu_id = input("Enter student Roll No. : = ")
        self.name = input("Enter name : =")
        self.email = input("Enter email : = ")
        self.gmail = "@gmail.com"
        while True:
            if self.gmail in self.email:
                break
            else:
                print("please enter Valid Email ID : ")
                self.email = input("Enter email : = ")
        self.course = input("Enter Course : = ")

class PremiumStudent(Student):
    student_list = {}
    def __init__(self,student_id,name,email,course,membership_level):
        super().__init__(student_id,course,name,email)
        print("1 : Beginner \n2 : Average \n3 : VIP")
        self.mem_level = int(input("Enter membership level : = "))#membership_level
        while True:
            if self.mem_level == 1 or self.mem_level == 2 or self.mem_level == 3:
                break
            else:
                print("Enter Correct Membership Level")
                print("1 : Beginner \n2 : Average \n3 : VIP")
                self.mem_level = int(input("Enter membership level : = "))

    def display_premium_details(self):
        print(f"{self.stu_id} | {self.name} | {self.email} | {self.course} | {self.mem_level}")

        self.student_list[self.stu_id] = (self.name,self.email,self.course,self.mem_level)
    @classmethod
    def print_students_list(cls):
        for key, value in PremiumStudent.student_list.items():
            print(f'{key}: {value}')



# p1 = PremiumStudent(000,"Name","Email_ID","Course",000)
# p1.display_premium_details()
# p1.print_students_list()
print("---------------------------E-learning Student Data---------------------------")
print("No data Available")
PremiumStudent.print_students_list()
n = 1
while n !=0:
    dict1 = {1: "New Student",2 : "Student List",0: "Exit"}
    for k, v in dict1.items():
        print(f"{k} = {v}")
    n = int(input("Enter choice : "))

    if n == 1:
        p1 = PremiumStudent(000,"Name","Email_ID","Course",000)
        p1.display_premium_details()
    elif n == 2:
        PremiumStudent.print_students_list()
    elif n == 0:
        PremiumStudent.print_students_list()
        print("EXIT")
    else:
        print("INVALID INPUT !!\n-------------------Enter Again-------------------")
        pass


