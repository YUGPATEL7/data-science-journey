class Demo:
    def __init__(self):
        self.Rollno =0
        self.name =""

    def ReadData(self):
        self.Rollno = int(input('Enter a Rollno'))
        self.name    = input('Enter a Name')

    def ShowData(self):
        print(self.Rollno,"\t",self.name)
        