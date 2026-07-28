from DemoClass import Demo 

studentList = []
for i in range(2):
    d = Demo()
    d.ReadData()
    studentList.append(d)


print("=======================")
for s in studentList:
    s.ShowData()