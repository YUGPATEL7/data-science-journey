# print("BIKE RENTAL SERVICES ")

# obj =[]
# user_input = int(input("How Many Customer You Want to Add "))

# for i in range(user_input):
#     Customer_Name = input("Enter your name ")
#     Mobile_No = input("Enter mobile no: ")
#     Bike_Name = input("Enter a Bike name")
#     Rent_per_Day = int(input("Enter Rent_per_Day: "))
#     Total_Day = int(input("Enter Total_Day: "))
#     Total = Rent_per_Day * Total_Day

#     data = [Customer_Name,Mobile_No,Bike_Name,Rent_per_Day,Total_Day,Total]
#     obj.append(data)

# print("No\tCustomer_Name\tMobile_No\tBike_Name\tRent_per_Day\tTotal_Day")
# for item in range(user_input):
#      print(f"{item+1}\t{obj[item][0]}\t\t{obj[item][1]}\t{obj[item][2]}\t{obj[item][3]}\t{obj[item][4]}\t{obj[item][5]}")

# total_no_day = sum(item[4] for item in obj )
# total_no_amount = sum(item[5] for item in obj )
# print("Total Weight" , total_no_day)
# print("Total Amount" , total_no_amount)

# yes_no = int(input("Are You Want to Print Data in Ascending Order By Rent or Days?:- for Rent - 1 \n days - 2  "))
# if(yes_no == 1):
#     print("Acceding By Rent ")

#     print("No\tCustomer_Name\tMobile_No\tBike_Name\tRent_per_Day\tTotal_Day")

#     sorted_by_rent = sorted(obj, key=lambda item:item[3])
#     for item in sorted_by_rent:
#         print(f"\t{item[0]}\t\t{item[1]}\t{item[2]}\t{item[3]}\t{item[4]}\t{item[5]}")
# elif(yes_no == 2):

#     sorted_by_amount = sorted(obj, key=lambda item:item[4])
#     for item in sorted_by_amount:
#         print(f"\t{item[0]}\t\t{item[1]}\t{item[2]}\t{item[3]}\t{item[4]}\t{item[5]}")
# else:
#     print((":)"))


    

students = ["Amit", "Ravi", "Priya", "Neha", "Karan"] 

temp = students.reverse()

print(temp)
print(students)