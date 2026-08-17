# class UniversityClass:
#     def __init__(self,uname,uid):
#         self.uname = uname
#         self.uid =uid

#     def u_show_data(self):
#         print(self.uname,self.uid)
# class CollegeClass(UniversityClass):
#     def __init__(self,uname,uid,cname,cid):
#         super().__init__(uname,uid)
#         self.cname = cname
#         self.cid =cid
#     def show_data(self):
#         super().u_show_data()
#         print(self.cname,self.cid)
# class StudentClass(CollegeClass):
#     def __init__(self,uname,uid,cname,cid,name,rollno):
#         super().__init__(uname,uid,cname,cid)
#         self.name = name
#         self.rollno =rollno

#     def show_data(self):
#         super().show_data()
#         print(self.name,self.rollno)

# s = StudentClass("GTU",12,"GPH",624,"yug",55)
# s.show_data()


# Pr 3 
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 
#     def show_data_person(self):
#         print("Name: ",self.name)
#         print("age: ",self.age)
# class student(person):
#     def __init__(self,name,age,per):
#         super().__init__(name,age)
#         self.per = per
#     def show_data_student(self):
#         print("Student")
#         super().show_data_person()
#         print("Per: ",self.per)

# class teacher(person):
#     def __init__(self,name,age,salary):
#             super().__init__(name,age)
#             self.salary = salary
#     def show_data_teacher(self):
#         print("Teacher")
#         super().show_data_person()
#         print("Salary: ",self.salary)
        

# s = student("Yug",18,80.99)
# t= teacher("Mr.Sumit",45,100000)
# s.show_data_student()
# t.show_data_teacher()

# Pr 4 tho public & private no che 

# Pr 7 
# class crickter:
#     def __init__(self,name,total_matches):
#         self.name = name
#         self.total_matches = ""
#     def read(self):
#         self.name = input("Enter your name: ")
#         self.total_matches = int(input('Enter your total matches: '))
    
# class batsman(crickter):
#     def __init__(self,name,total_matches,total_runs,avg_runs,best_performance):
#         super().__init__(name,total_matches)
#         self.total_runs = total_runs
#         self.avg_runs = avg_runs
#         self.best_performance =best_performance

#     def calculate(self):
#         self.avg_runs = self.total_runs/self.total_matches
#     def show(self):
#         self.calculate()
#         print("Total Matches",self.total_matches)
#         print("Total Runs",self.total_runs)
#         print("Avg",self.avg_runs)
#         print("Best performance",self.best_performance)

# b = batsman("",0,9876,0,189)
# b.read()
# print("You have entered")
# b.show()



         



