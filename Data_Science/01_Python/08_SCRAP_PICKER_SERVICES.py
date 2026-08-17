print("SCRAP PICKER SERVICES 🏎️🏎️")
obj = []
user_name = input("Naam Enter kar na bhai ")
moblie = input("Phone hoo to number be enter kar na")
city = input("Aapne jinda ge kaha kat raha ha ")
adderss  = input("Ghar ho to adderss enter kar na ")

no_of_scrap = int(input("Bata bahi kit na bhagar enter kar na ha "))

for i in range(no_of_scrap):

    Scrap_Type = input("Enter your scrap type ")
    Weight = int(input("Enter Weight: "))
    Amount = int(input("Enter Amount: "))
    Total_Amount = Weight * Amount

    scrap = [Scrap_Type, Weight, Amount, Total_Amount]
    obj.append(scrap)

print(obj)


print("Customer Name", user_name)
print("Mobile", moblie)
print("city", city)
print("address", adderss)

print("No\tScrapType\tWeight\tAmount\tTotal Amount")
for item in range(no_of_scrap):
     print(f"{item+1}\t{obj[item][0]}\t\t{obj[item][1]}\t{obj[item][2]}\t{obj[item][3]}")
    
total_weight = sum(item[1] for item in obj)
total_amount = sum(item[2] for item in obj)
print("Total Weight" , total_weight)
print("Total Amount" , total_amount)
    

sort_by=input("Are You Want to Print Data in Ascending Order By Weight[1] or Amount[2]? ")
if(sort_by  == '1'):
    sort_by_weight = sorted(obj,key=lambda item:item[1])
    print(" Acceding By Weight ")
    print("No\tScrapType\tWeight\tAmount\tTotal Amount")
    for i, item in enumerate(sort_by_weight, start=1):
        print(f"{i}\t{item[0]}\t\t{item[1]}\t{item[2]}\t{item[3]}")
elif(sort_by  == '2'):
    sort_by_Amount = sorted(obj,key=lambda item:item[2])
    print(" Acceding By Amount ")
    print("No\tScrapType\tWeight\tAmount\tTotal Amount")
    for i, item in enumerate(sort_by_Amount, start=1):
        print(f"{i}\t{item[0]}\t\t{item[1]}\t{item[2]}\t{item[3]}")

print("Total Weight" , total_weight)
print("Total Amount" , total_amount)
