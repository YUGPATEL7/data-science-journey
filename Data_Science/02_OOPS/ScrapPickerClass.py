import re
import json
class ScrapPicker:
    def read_data(self):
        with open(r"Data Science\Text_Files\scrappicker.txt", "r") as f:
            sp = json.load(f)
        string_pattern = '[a-zA-Z\\s]{1,50}$'
        user_name = input("Naam Enter kar na bhai ")
        while(re.match(string_pattern,user_name) is None):
            print("This file only contain alphabets")
            user_name = input(f"Re-Enter your name : ")
        
        city = input("Aapne jinda ge kaha kat raha ha ")
        while(re.match(string_pattern,city) is None):
            print("This file only contain alphabets")
            city = input(f"Re-Enter your city : ")
        number_pattern = r'^\d{10}'
        mobile = input("Phone hoo to number be enter kar na")
        while(re.match(number_pattern,mobile) is None):
            print("This file only contain number up to 10 digits")
            moblie = input(f"Re-Enter your mobile number : ")
        address  = input("Ghar ho to adderss enter kar na ")
        no_of_scrap = int(input("Bata bahi kit na bhagar enter kar na ha "))

        for i in range(no_of_scrap):

            Scrap_Type = input("Enter your scrap type ")
            Weight = int(input("Enter Weight: "))
            Amount = int(input("Enter Amount: "))
            Total_Amount = Weight * Amount
            if sp:
                next_id = str(max(map(int, sp.keys())) + 1)
            else:
                next_id = "1"
            sp[next_id] = {
                "name": user_name,
                "city": city,
                "mobile": mobile,
                "address": address,
                "scrap_info": []
            }
            sp[next_id]["scrap_info"].append({
            "scrap_type": Scrap_Type,
            "weight": Weight,
            "amount": Amount,
            "total_amount": Total_Amount
            })
            with open(r"Data Science\Text_Files\scrappicker.txt", "w") as f:
                json.dump(sp, f, indent=4)

    def show_data(self):
        with open(r"Data Science\Text_Files\scrappicker.txt", "r") as f:
            sp = json.load(f)

        for customer_id, customer in sp.items():

            print("-" * 60)
            print("Customer ID :", customer_id)
            print("Customer Name :", customer["name"])
            print("Mobile :", customer["mobile"])
            print("City :", customer["city"])
            print("Address :", customer["adderss"])

            print("\nNo\tScrap Type\tWeight\tAmount\tTotal Amount")

            total_weight = 0
            grand_total = 0

            for i, scrap in enumerate(customer["scrap_info"], start=1):
                print(
                    f"{i}\t{scrap['scrap_type']}\t\t"
                    f"{scrap['weight']}\t"
                    f"{scrap['amount']}\t"
                    f"{scrap['total_amount']}"
                )

                total_weight += scrap["weight"]
                grand_total += scrap["total_amount"]

            print("-" * 60)
            print("Total Weight :", total_weight)
            print("Grand Total  :", grand_total)
            print("-" * 60)