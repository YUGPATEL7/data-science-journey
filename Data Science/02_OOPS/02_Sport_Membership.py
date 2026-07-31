from SportMembershipClass import SportMembership

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

customer_info = {}
print("Welcome to use Sport Membership Calualtor :) ")
no_of_itration = int(input('Enter how many customer you have to enter now: '))

for c_id,detahils in customer_info.items():
    customer_id = c_id



for i in range(no_of_itration) :
    customer_id+=1
    s.read_data(i)
    charge =s.charges() * s.is_offer_apply  

    print(f"\t\tThe membership of fee from {s.name} is {charge}")
    print("------------------------------------------------------")
    customer_info[customer_id]={
        "name":s.name,
        "months":s.months,
        "special_offer":s.special_offer,
        "fee":charge,
    }
    

print("Summary of Membership Fee")
print("=================================================")
print("Name\tMonths\tSpecialOffer\tCharge")
print("------------------------------------------------------")
s.show_data(customer_info)
print ("Thank you for using Sport Membership Calualtor :)")


