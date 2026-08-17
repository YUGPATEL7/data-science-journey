print("Welcome to E-Bookshop :) ")
No_Books = int(input('How Many Books You Want to Enter'))

obj = []

for i in range(No_Books):
    Author = input("Enter Author name ")
    Book_Name = input("Enter Book name ")
    Price = int(input("Enter Price "))
    Publisher = input("Enter Publisher ")
    Stock = int(input("Enter Stock "))
    Total = Price* Stock
    if Stock < 5:
        Notification = "Less Than 5 Stock"
    elif Stock > 20:
        Notification = "Greater Than 20"
    else:
        Notification = "-"
        
    book = {
            'Author': Author,
            'Book_Name': Book_Name,
            'Price': Price,
            'Publisher': Publisher,
            'Stock': Stock,
            'Total': Total,
            'Notification': Notification
        }
    obj.append(book)

# print(obj)

print("No\tAuthor\tBook Name\tPrice\tPublisher\tStock\tTotal\tNotification")

for item in range(No_Books):
    print("----------------------------------------------------------------------------")
    print(f"{item+1}\t{obj[item]['Author']}\t{obj[item]['Book_Name']}\t{obj[item]['Price']}\t{obj[item]['Publisher']}\t{obj[item]['Stock']}\t{obj[item]['Total']}\t{obj[item]['Notification']}")


Order = input("Please Enter Ascending Order Option By Input Enter:\n1. For Price\n2. For Qty  ")
print("Enter Your Option -",Order)
print("After Ascending Order List: ")

print("No\tAuthor\tBook Name\tPrice\tPublisher\tStock\tTotal\tNotification")
for item in range(No_Books):
    print("----------------------------------------------------------------------------")

    if (Order == "1"):
        sorted_books  = sorted(obj,key=lambda item:item['Price'])
        for item in sorted_books:
            print(f"{item}\t{item['Author']}\t{item['Book_Name']}\t{item['Price']}\t{item['Publisher']}\t{item['Stock']}\t{item['Total']}\t{item['Notification']}")
    elif(Order == "2"):
        sorted_books  = sorted(obj,key=lambda item:item['Stock'])
        for item in sorted_books:
            print(f"{item}\t{item['Author']}\t{item['Book_Name']}\t{item['Price']}\t{item['Publisher']}\t{item['Stock']}\t{item['Total']}\t{item['Notification']}")
    else:
        print("Do not enter anything expect 1 & 2 :)")