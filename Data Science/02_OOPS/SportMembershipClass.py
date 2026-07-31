class SportMembership :
    def __init__(self):
        self.M = 4
        self.name = "" 
        self.months = 0
        self.special_offer = ""
        self.charge = 0 
        self.per_month = 0
        self.is_offer_apply = 1

    def read_data(self,i):
        self.name = input(f"Enter your name {i}: ")
        self.months = int(input('Enter the number of months: '))
        while self.months < 1 or self.months > 60:
            self.months = int(input("Months should be between 1 and 60. Enter again: "))
        self.special_offer = input("Enter yes or no to indicate a special offer: ")
        if(self.special_offer == "yes"):
            self.is_offer_apply = 0.85

    def charges(self):
        if self.months < 6:
            return self.months * 30
        elif self.months < 12:
            return self.months * 27.5
        else:
            return self.months * 25

    def show_data(self,customer_info):
        max_fee = 0
        max_name = ""
        min_fee = 0
        min_name = ""
        ls_six = ""
        gt_six = ""
        for pas,c in customer_info.items():
            print(f"{c['name']} \t {c['months']} \t {c['special_offer']} \t\t ${c['fee']}")

            if c["fee"] < min_fee:
                min_fee = c["fee"]
                min_name = c["name"]
            if c["fee"] > max_fee:
                max_fee = c["fee"]
                max_name = c["name"]
            
            
            if(c['months'] < 6):
                ls_six+="x"
            else:
                gt_six+="x"
        print("------------------------------------------------------")
        print(f"The customer spending most is {max_name} ${max_fee} ")
        print(f"The customer spending least is {min_name} ${min_fee} ")
        print("The number of member with < 6 months" , ls_six)
        print("The number of member with >= 6 months" , gt_six)
        
        

