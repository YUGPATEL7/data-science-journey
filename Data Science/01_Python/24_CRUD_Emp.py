from datetime import date
today = date.today()
formatted_date = today.strftime("%d/%m/%Y")
print("Welcome to employee management system")
# emp_dict= {}
emp_dict = {
    "EMP001": {
        "Name": "Yug Patel",
        "Email": "yug@gmail.com",
        "Phone": "123",
        "Entry_Date": "2026-07-27"
    },
    "EMP002": {
        "Name": "Om Patel",
        "Email": "om@gmail.com",
        "Phone": "9988776655",
        "Entry_Date": "2026-07-28"
    }
}
def Emp_Menu():
    print("Pleasa Select Option From Below For CRUD Opration in Employee Managment System :-")
    print("1. Get Employee List ")
    print("2. Get Employee By EmpID")
    print("3. Add New Employee")
    print("4. Update Employee by Id :- Name , E-mail , Phone")
    print("5. Delete Employee by Id")
    print("6.Exit Software")

def Emp_list():
    print("ID\t Name \t\t PhoneNo. \t E-mail \t Entry_Date")
    for emp_id, details in emp_dict.items():
        print(f"{emp_id} \t {details['Name']} \t {details['Phone']} \t { details['Email']} \t { details['Entry_Date']}")

def Emp_by_id(emp_id_by_user):
    for emp_id, details in emp_dict.items():
        if(emp_id_by_user ==  emp_id):
            print("ID\t Name \t\t PhoneNo. \t E-mail \t Entry_Date")
            print(f"{emp_id} \t {details['Name']} \t {details['Phone']} \t { details['Email']} \t { details['Entry_Date']}")
            return
    else:
        print("Emp data is not found")

def IsNumber_Exist(Phone):
    for details in emp_dict.values():
        if details["Phone"] == Phone:
            Phone = input("Phone already exists. Enter another phone number: ")
            break

def IsEmail_Exist(Email):
    for details in emp_dict.values():
        if details["Email"] == Email:
            Email = input("Email already exists. Enter another email : ")
            break
num = 0

while True:
    
    Emp_Menu()

    num = int(input('Enter a num : '))

    if(num == 1):
        Emp_list()

    elif(num == 2):
        emp_id_by_user = input('Enter a emp id that you have to search: ')
        Emp_by_id(emp_id_by_user)

    elif(num == 3):
        Emp_id = input("Enter ID: ")
        Name = input("Enter Name: ")
        Email = input("Enter Email: ")
        Phone = input("Enter Phone: ")
        IsNumber_Exist(Phone)
        IsEmail_Exist(Email)
        emp_dict[Emp_id] = {
            "Name": Name,
            "Email": Email,
            "Phone": Phone,
            "Entry_Date":formatted_date
        }

    elif(num == 4):
        emp_id_by_user = input('Enter a emp id that you have to update: ')
        for emp_id, details in emp_dict.items():
            if(emp_id_by_user ==  emp_id):
                Name = input("Enter Name: ")
                Email = input("Enter Email: ")
                Phone = input("Enter Phone: ")
                formatted_date=details['Entry_Date'] 
                IsNumber_Exist(Phone)
                IsEmail_Exist(Email)
                emp_dict[emp_id_by_user] = {
                    "Name": Name,
                    "Email": Email,
                    "Phone": Phone,
                    "Entry_Date":formatted_date
                }
        else:
            print("Emp data is not found")
        
    elif(num == 5):
        emp_id_by_user = input('Enter a emp id that you have to delete: ')
        if emp_id_by_user in emp_dict:
            del emp_dict[emp_id_by_user]
            print("Employee deleted successfully.")
        else:
            print("Emp ID is not found")


    elif(num == 6):
            print("Thank you for using the emp management")
            break

        

