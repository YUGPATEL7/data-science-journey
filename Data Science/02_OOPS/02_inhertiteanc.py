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


# Pr 1 Simple inheritance

class Base:
    def __init__(self, x=0):
        self.x = x
    def puls(self):
        self.x += 1
    def show_data(self):
        print("Value of x:", self.x)

class Derived(Base):
    def __init__(self,x):
        super().__init__(x)
    def show_data1(self):
        x=x-1
        super().show_data()
        print("Value of x:", self.x)

d = Derived(7)
d.puls()
d.show_data()
d.show_data1()