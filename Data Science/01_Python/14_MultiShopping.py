# no_of_user =int(input('How Many Customer You Want to Add?'))

customers = {
    "yug": [
        {
            "Pname": "Laptop",
            "Price": 1,
            "Qty": 50
        },
        {
            "Pname": "TV",
            "Price": 10,
            "Qty": 100
        },
        {
            "Pname": "TV",
            "Price": 2,
            "Qty": 100
        }
    ],
    "om": [
        {
            "Pname": "Book",
            "Price": 200,
            "Qty": 5
        },
        {
            "Pname": "note",
            "Price": 20,
            "Qty": 5
        }
    ]
}

count = 1
no = 1
total = 0
grand_total = 0
Discount= 0
net_total = 0
print("===========================================================")
for customer, products in customers.items():
    print(f"#{count}. Customer Name : {customer}")
    print("No\tName\tPrice\tQty\tTotal")
    print("===========================================================")
    for product in products:
        total = product["Price"]*product["Qty"]
        grand_total+=total
        Discount = grand_total*0.10
        net_total = grand_total - Discount
        print(f"{no}\t{product['Pname']}\t{ product['Price']}\t{product['Qty']}\t{total}")
        no+=1
    print(f"Grand Total = {grand_total}\nDiscount (10%)= {Discount}\nNet Total = {net_total}")
        
    print("Thanks For Shopping.")
    print("===========================================================")
        

    
