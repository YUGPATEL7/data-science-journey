from BookSellerClass import BookSeller

b = BookSeller()

obj_books = {
    1:{
        "authour" : "Balaguru",
        "book_name":"C++",
        "price" :100,
        "publisher" : "yug",
        "stock":4,
        "total" : 0,
        "notification" : ""
    },
    2:{
        "authour" : "Balaguru",
        "book_name":"C++",
        "price" :45,
        "publisher" : "om",
        "stock":4,
        "total" : 0,
        "notification" : ""
    }
}
b.read_data()
b.show_data()
b.order()