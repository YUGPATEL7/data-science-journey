import re
class SportMembership :
    # Constructor used to initialize the instance variables.
    def __init__(self):
        self.M = 4
        self.name = "" 
        self.months = 0
        self.special_offer = ""
        self.charge = 0 
        self.per_month = 0
        self.is_offer_apply = 1

    # This method reads and validates the customer details.
    def read_data(self,i):
        name_pattern = '[a-zA-Z\\s]{1,50}$'
        self.name = input(f"Enter your name at {i} ID : ")
        # Validate that the name contains only alphabets and spaces
        # with a length between 1 and 50 characters.      
        while (re.match(name_pattern,self.name)) is None:
            print("Name should contain only alphabets")
            self.name = input(f"Re-Enter your name {i}: ")

        self.months = int(input('Enter the number of months: '))
        # Validate that the membership duration is between 1 and 60 months.
        while self.months < 1 or self.months > 60:
            self.months = int(input("Months should be between 1 and 60. Enter again: "))
        # Check whether the customer is eligible for a special offer.
        self.special_offer = input("Enter yes or no to indicate a special offer: ")
        # Apply a 15% discount if the customer has a special offer.
        if self.special_offer.lower() == "yes":
            self.is_offer_apply = 0.85
        else:
            self.is_offer_apply = 1

    # Calculate the membership fee based on the membership duration.
    def charges(self):
        if self.months <= 6:
            return self.months * 30
        elif self.months <= 12:
            return self.months * 27.5
        else:
            return self.months * 25

    # Display the membership details, highest and lowest spending customers,
    # and a simple bar chart based on membership duration.
    def show_data(self,customer_info):
        max_fee = customer_info[1]["fee"]
        max_name = customer_info[1]["name"]
        min_fee = customer_info[1]["fee"]
        min_name = customer_info[1]["name"]
        ls_six = ""
        gt_six = ""
        #  Display each customer's information.
        for _,c in customer_info.items():
            print(f"{c['name']} \t {c['months']} \t {c['special_offer']} \t\t ${c['fee']}")
        # Min spent by customer
            if c["fee"] < min_fee:
                min_fee = c["fee"]
                min_name = c["name"]
        # Max spent by customer
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
        
        

