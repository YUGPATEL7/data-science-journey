user_name=input("Please Enter Customer Name: ")
no_of_product = int(input("How Many Products You Want to Add?"))


details_of_product = []
count = 1
for i in range (no_of_product):
    print(f"#{count}")
    Name = input("Please Enter Product Name:")
    Price =int(input("Please Enter Product Price:"))
    Qty = int(input("Please Enter Product Qty:"))
    count+=1
    product_Info= {
        "Name":Name,
        "Price":Price,
        "Qty":Qty
    }
    details_of_product.append(product_Info)

print("===========================================================")
print("Customer Name :",user_name)
print("===========================================================")
print("No\tName\tPrice\tQty	Total")
count = 1
Grand_Total=0
for data in details_of_product:
    item_total = data['Price']*data['Qty']
    Grand_Total+=item_total
    print(f"{count}\t{data['Name']}\t{data['Price']}\t{data['Qty']}\t{item_total} ")
    count+=1
print("===========================================================")

Net_Total = Grand_Total * 0.90
print("Grand Total: ",Grand_Total)
print("Discount (10%): ",Grand_Total-Net_Total)
print("Net Total: ",Net_Total)
print("Thanks For Shopping.")