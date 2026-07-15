employees = [ ["EMP001","Amit Patel",25000,"IT"], ["EMP002","Priya Shah",30000,"HR"], ["EMP003","Rohit Kumar",-5000,"IT"], ["EMP004","Neha Joshi",45000,"Finance"], ["EMP005","",28000,"HR"], ["EMP006","Raj Mehta",None,"IT"], ["EMP007","Karan Singh",35000,"Sales"], ["EMP008","Pooja Patel",0,"Marketing"], ["EMP009","Amit Patel",25000,"IT"], ["EMP010","Meena Desai",50000,""],  ["EMP011","Riya Sharma",32000,"HR"], ["EMP012","Vikas Patel",27000,"IT"], ["EMP013","Sneha Shah",42000,"Finance"], ["EMP014","Nirav Mehta",39000,"Sales"], ["EMP015","Anjali Patel",31000,"Marketing"], ["EMP016","Dhruv Shah",29000,"IT"], ["EMP017","Krunal Patel",34000,"HR"], ["EMP018","Jinal Shah",36000,"Finance"], ["EMP019","Parth Mehta",41000,"Sales"], ["EMP020","Nidhi Patel",38000,"Marketing"],  ["EMP021","Harsh Shah",26000,"IT"], ["EMP022","Bhavik Patel",27500,"HR"], ["EMP023","Komal Shah",33000,"Finance"], ["EMP024","Yash Mehta",37000,"Sales"], ["EMP025","Mansi Patel",35000,"Marketing"], ["EMP026","Dev Shah",45000,"IT"], ["EMP027","Isha Patel",48000,"HR"], ["EMP028","Jay Mehta",29000,"Finance"], ["EMP029","Kajal Shah",31000,"Sales"], ["EMP030","Manav Patel",34000,"Marketing"], ["EMP031","Aarav Shah",30000,"IT"], ["EMP032","Diya Patel",32000,"HR"], ["EMP033","Vivaan Mehta",36000,"Finance"], ["EMP034","Kiara Shah",38000,"Sales"], ["EMP035","Aditya Patel",42000,"Marketing"], ["EMP036","Riddhi Shah",27000,"IT"], ["EMP037","Tushar Mehta",46000,"HR"], ["EMP038","Pallavi Patel",39000,"Finance"], ["EMP039","Sagar Shah",35000,"Sales"], ["EMP040","Hetal Mehta",31000,"Marketing"], ["EMP041","Amit Patel",25000,"IT"], ["EMP042","Priya Shah",30000,"HR"], ["EMP043","",41000,"Finance"], ["EMP044","Raj Mehta",None,"Sales"], ["EMP045","Neha Joshi",-10000,"Marketing"], ["EMP046","Harsh Patel",36000,"IT"], ["EMP047","Naina Shah",34000,"HR"], ["EMP048","Vivek Mehta",43000,"Finance"], ["EMP049","Krisha Patel",39000,"Sales"], ["EMP050","Devanshi Shah",28000,""], ["EMP051","Mihir Patel",31000,"IT"], ["EMP052","Ruchi Shah",33000,"HR"], ["EMP053","Ankit Mehta",37000,"Finance"], ["EMP054","Bhumi Patel",40000,"Sales"], ["EMP055","Chirag Shah",45000,"Marketing"], ["EMP056","Dhwani Mehta",47000,"IT"], ["EMP057","Esha Patel",29000,"HR"], ["EMP058","Falgun Shah",31000,"Finance"], ["EMP059","Gaurav Mehta",35000,"Sales"], ["EMP060","Hiral Patel",38000,"Marketing"], ["EMP061","Ishan Shah",26000,"IT"], ["EMP062","Janki Patel",28000,"HR"], ["EMP063","Ketan Mehta",34000,"Finance"], ["EMP064","Lina Shah",36000,"Sales"], ["EMP065","Milan Patel",39000,"Marketing"], ["EMP066","Nilesh Shah",42000,"IT"], ["EMP067","Ojas Mehta",44000,"HR"], ["EMP068","Pinal Patel",46000,"Finance"], ["EMP069","Rakesh Shah",30000,"Sales"], ["EMP070","Sonal Mehta",32000,"Marketing"], ["EMP071","Tanvi Patel",35000,"IT"], ["EMP072","Umesh Shah",37000,"HR"], ["EMP073","Vaibhav Mehta",41000,"Finance"], ["EMP074","Yamini Patel",43000,"Sales"], ["EMP075","Zarna Shah",48000,"Marketing"], ["EMP076","Aakash Mehta",29000,"IT"], ["EMP077","Bhavna Patel",31000,"HR"], ["EMP078","Chetan Shah",34000,"Finance"], ["EMP079","Deepa Mehta",36000,"Sales"], ["EMP080","Eshan Patel",40000,"Marketing"], ["EMP081","Farhan Shah",45000,"IT"], ["EMP082","Geeta Mehta",47000,"HR"], ["EMP083","Hemal Patel",28000,"Finance"], ["EMP084","Ila Shah",30000,"Sales"], ["EMP085","Jigar Mehta",33000,"Marketing"], ["EMP086","Kush Patel",35000,"IT"], ["EMP087","Lavina Shah",38000,"HR"], ["EMP088","Mitesh Mehta",42000,"Finance"], ["EMP089","Nisha Patel",44000,"Sales"], ["EMP090","Om Shah",46000,"Marketing"], ["EMP091","Parul Mehta",27000,"IT"], ["EMP092","Qadir Patel",29000,"HR"], ["EMP093","Rina Shah",32000,"Finance"], ["EMP094","Smit Mehta",35000,"Sales"], ["EMP095","Tina Patel",39000,"Marketing"], ["EMP096","Urvashi Shah",41000,"IT"], ["EMP097","Viral Mehta",45000,"HR"], ["EMP098","Waseem Patel",47000,"Finance"], ["EMP099","Yogesh Shah",50000,"Sales"], ["EMP100","Zeeshan Mehta",52000,"Marketing"], ["EMP101","Amit Patel",25000,"IT"], ["EMP102","",None,"HR"], ["EMP103","Raj Mehta",-7000,"Finance"], ["EMP104","Pooja Patel",0,"Marketing"], ["EMP105","Sneha Shah",42000,"Finance"] ]

# Part A: List Operations 

# Q1 Find the total number of employee records. 
# print(len(employees))

# # Q2. Add a new employee record. 
# employees.extend(["EMP011", "Riya Sharma", 32000, "HR"] )
# print(employees.count("EMP011"))

# # Q3. Remove employee EMP008 from the list. 
# for emp in employees:
#     if emp[0]  == "EMP008":
#         employees.remove(emp)
#         print("Done")
#         break

# Q4. Display all employee names only. 
# for emp in employees : 
#     print(emp[1])

# Q5. Find employees whose salary is greater than ₹30,000. 
# for emp in employees : 
#     if emp[2] is not None and emp[2] >= 30000:
#         print(emp)
#     else:
#         pass

# Part B: Data Cleaning Using List 
# Q6. Find records having blank employee names. 
# for emp in employees:
#     if emp[1] is ""  :
#         print(emp)
#     else:
#         pass
# # Q7. Find records having blank department names. 
# for emp in employees:
#     if emp[3] is ""  :
#         print(emp)
#     else:
#         pass

# Q8. Find records having NULL salary values. 
# for emp in employees:
#     if emp[2] is None  :
#         print(emp)
#     else:
#         pass

# # Q9. Find records having negative salary values. 
# for emp in employees:
#     if emp[2] is not None and emp[2] < 0  :
#         print(emp)
#     else:
#         pass

# Q10. Replace negative salary with 0. 
# for emp in employees:
#     if emp[2] is not None and emp[2] < 0  :
#         emp[2] = 0
#         print(emp)
#     else:
#         pass

# Q11. Replace NULL salary with average salary of valid employees. 
# total = 0 
# count = 0
# for emp in employees:
#     if emp[2] is not None:
#         total+=emp[2]
#         count+=1
# avg = total / count
# for emp in employees:
#     if emp[2] is None :
#         emp[2] = avg
#         print(emp)
#     else:
#         pass

# Q12. Remove records having blank employee names. 
# for emp in employees:
#     if emp[2] is None or emp[1] == "":
#         print(emp)
#         employees.remove(emp)
#     else:
#         pass


# Part C: Tuple Operations 


# Q13. Convert all employee records into tuple format. 
# tuple_emp = tuple(employees)
# print(tuple_emp)

# Q14. Display Employee ID and Name using tuple indexing. 
# for emp in tuple_emp:
#     print("Name:",emp[1],"Emp ID ", emp[0])

# Q15. Count total tuple records. 
# print(len(tuple_emp))

# Q16. Find highest salary employee using tuples.
# highest  = max(tuple_emp,key=lambda x:x[2] if x[2] is not None else 0 )
# print("Highest Salary:", highest[2])

# Q17. Find lowest salary employee using tuples. 
# lowest = min(tuple_emp, key=lambda x:x[2] if x[2] is not None else 0)
# print(lowest)

# Part D: Set Operations 


# Q18. Create a set of all departments.
# set_emp= {emp[3] for emp in employees}
# print(set_emp)

# Q19. Display unique department names.
# print(set_emp)

# Q20. Count total unique departments. 
# print(len(set_emp))
# Q21. Check whether "Finance" department exists or not. 
# if "Finance" in set_emp:
#     print("yes")
# else:
#     print("No")
    

# Q22. Add a new department "Administration". 
# set_emp.add("Administration")
# print(set_emp)

# Q23. Remove "Marketing" department.
# set_emp.discard("Marketing")
# print(set_emp) 

# Part E: Duplicate Data Cleaning Using Set
# Q24. Identify duplicate employee names.
# set_emp_name = {emp[1] for emp in employees}
# duplicate = set()
# seen = set()

# 2. Loop through and find duplicates
# for emp_name in employees:
#     name = emp_name[1]
#     if name in seen:
#         duplicate.add(name)
#     else:
#         seen.add(name)
# print("Duplicate employee names:", duplicate)

# Q25. Create a set of employee names. 
# print(set_emp_name)

# Q26. Count unique employees. 
# print(len(set_emp_name))

# Q27. Find duplicate records. Expected Duplicate: "Amit Patel" 
# print(seen)

# Part F: Data Analysis 
# Q28. Calculate total salary expenditure. & # Q29. Calculate average salary. 
# total = 0 
# count = 0
# for emp in employees:
#     if emp[2] is not None:
#         total+=emp[2]
#         count+=1
# avg = total / count
# for emp in employees:
#     if emp[2] is None :
#         emp[2] = avg
#         print(emp)
#     else:
#         pass


# Q30. Find maximum salary.
# total = max(employees, key =lambda x:x[2] if x[2] is not None else 0)
# print(total[2])

#  Q31. Find minimum salary. 
# total = min(employees, key =lambda x:x[2] if x[2] is not None else 0)
# print(total[2])


# Part G: Mini Project Employee Data Cleaning Report Perform the following: 
# ✔ Remove duplicate employee names
# ✔ Remove blank names 
# ✔ Replace NULL salary with average salary
#  ✔ Replace negative salary with 0
#  ✔ Replace blank department with "Unknown"
#  ✔ Generate Final Clean Dataset
# ✔ Display: • Total Employees  • Total Departments  • Total Salary  • Average Salary  • Highest Salary Employee  • Lowest Salary Employee  


# Bonus Challenge Create the following functions:
# def clean_salary(data):
#      pass
# def remove_duplicates(data):
#      pass
# def find_average_salary(data):
#     pass
# def generate_report(data):     
#      pass 