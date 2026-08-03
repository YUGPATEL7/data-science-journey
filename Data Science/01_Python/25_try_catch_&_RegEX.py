# try:
#     c =12/0
# except Exception as e :
#     print(e,":)")

# print("Continu the flow of program ")

# try:  
#     # code that may cause errors  
# except:
#     # code that handle exceptions 
# else:  
#     # code that executes when no exception occurs


import re
# name_pattern = '[a-zA-Z\\s]{1,50}$'
# name = input("Enter your name: ")
# if (re.match(name_pattern,name)) != None:
#     print("name is correct")
# else:
#     print("Name should contain only alpabats")
    
# mobileNo_pattern = "^\d{10}$"
# mobileNo = input("Enter your Mobile NO.: ")
# while re.match(mobileNo_pattern, mobileNo) is None:
#     print("Mobile No. should contain exactly 10 digits.")
#     mobileNo = input("RE-Enter your Mobile NO.: ")
# print("Mobile No. is correct ")



# Biodata
# name_pattern = '[a-zA-Z\\s]{1,50}$'
# num_pattern = "^\d{10}$"
# age_pattern = r'^(1[89]|[2-6][0-9]|70)$'
# name  = input("Enter you name ")
# while (re.match(name_pattern,name)) is None:
#     print("Name should contain only alpabats")
#     name  = input("Re-Enter you name ")

# num  = input("Enter you Number ")
# while (re.match(num_pattern,num)) is None:
#     print("Number should contain only 10 digits")
#     num  = input("Re-Enter you Number ")

# age  = input("Enter you age ")
# while (re.match(age_pattern,age)) is None:
#     print("Re-Enter Age From 18 to 70")
#     age  = input("Re-Enter you age ")

# password_pattern = r'^(?=.*[^A-Za-z0-9]).{8,20}$'

# password = input("Please Enter Your Password (Min 1 Capital, 1 Digit, 1 Small, 1 Special Symbol, 8-20 Characters): ")

# while re.fullmatch(password_pattern, password) is None:
#     print("Invalid Password.")
#     password = input("Please Re-Enter Password: ")

# print("Password Accepted!")

email_pattern =r'^(?=.+@gmail.com).{8,20}$'
email = input("Please Enter Your Email: ")

while re.fullmatch(email_pattern, email) is None:
    print("Invalid Password.")
    password = input("Please Re-Enter Password: ")








