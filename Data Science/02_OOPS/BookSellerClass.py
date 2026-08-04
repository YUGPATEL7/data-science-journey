import json
class BookSeller:
    def __init__(self):
        self.author = ""
        self.book_name=""
        self.price = 0
        self.publisher = ""
        self.stock = 0
        self.total = 0
        self.notification = ""

    def read_data(self):
        with open(r"Data Science\Text_Files\bookseller.txt", "r") as f:
            books = json.load(f)

        self.author = input("Author: ")
        self.book_name = input("Book Name: ")
        self.price = int(input("Price: "))
        self.publisher = input("Publisher: ")
        self.stock = int(input("Stock: "))
        self.total = self.price * self.stock
        if books:
            next_id = str(max(map(int, books.keys())) + 1)
        else:
            next_id = "1"
        books[next_id] = {
            "author": self.author,
            "book_name": self.book_name,
            "price": self.price,
            "publisher": self.publisher,
            "stock": self.stock,
            "total": self.total,
            "notification": ""
        }
        with open(r"Data Science\Text_Files\bookseller.txt", "w") as f:
            json.dump(books, f, indent=4)


    def show_data(self):
        with open(r"Data Science\Text_Files\bookseller.txt", "r") as f:
            books = json.load(f)
        gt_20 = 0
        ls_20 = 0
        print("No\tAuthor\tBook Name\tPrice\tPublisher\tStock\tTotal\tNotification")
        for key,values in books.items():
            print("----------------------------------------------------------------------------")
            print(key)
            print(f"{values['author']}\t{values['book_name']}\t{values['price']}\t{values['publisher']}\t{values['total']}\t{values['notification']}")
            if(values['stock'] < 5):
                ls_20+=1
            elif(values['stock']>20):
                gt_20+=1
        print("Greater Then 20 Stock – ",gt_20)
        print("Less Then 5 Stock – ",ls_20)


    def order(self):
        with open(r"Data Science\Text_Files\bookseller.txt", "r") as f:
            books = json.load(f)
        user_input=int(input("Please Enter Ascending Order Option By Input Enter: 1. For Price 2. For Qty  : "))
        if user_input == 1 :
            sorted_books = sorted(books.values(), key=lambda x: x["price"])
            for values in sorted_books:
                print(f"{values['author']}\t{values['book_name']}\t{values['price']}\t{values['publisher']}\t{values['total']}\t{values['notification']}")

        elif(user_input == "2"):
            sorted_books  = sorted(books.values(),key=lambda item:item['stock'])
            for values in sorted_books:
                print(f"{values['author']}\t{values['book_name']}\t{values['price']}\t{values['publisher']}\t{values['total']}\t{values['notification']}")
        else:
            print("Do not enter anything expect 1 & 2 :)")
        