from SportMembershipClass import SportMembership
M = 6

#Object used to initialize the instance 
s = SportMembership()

customer_id = 0
# customer_info = {
#     1:{
#         "name":"yug",
#         "months":5,
#         "special_offer":"no",
#         "fee":150,

#     },
#     1:{
#         "name":"patel",
#         "months":12,
#         "special_offer":"yes",
#         "fee":275   ,

#     },
#     4:{
#         "name":"harsh",
#         "months":5,
#         "special_offer":"no",
#         "fee":150,

#     },
#     5:{
#         "name":"om",
#         "months":5,
#         "special_offer":"no",
#         "fee":150,

#     }
# }

# Declaring the customer info.that use to store the customer info 
customer_info = {}
print("Welcome to the Sport Membership Calculator! ")

# It is used to track customer ID. 
for c_id,detahils in customer_info.items():
    customer_id = c_id

# For loop is iterating up to the M time and store the customer info. 
for i in range(M) :
    customer_id+=1
    s.read_data(i)
    charge =s.charges() * s.is_offer_apply  
    print(f"\t\tThe membership fee for {s.name} is {charge}")
    print("------------------------------------------------------")
    customer_info[customer_id]={
        "name":s.name,
        "months":s.months,
        "special_offer":s.special_offer,
        "fee":charge,
    }
    

# It's shows the summary
print("Summary of Membership Fee")
print("=================================================")
print("Name\tMonths\tSpecialOffer\tCharge")
print("------------------------------------------------------")
s.show_data(customer_info)
print ("Thank you for using Sport Membership Calualtor :)")


