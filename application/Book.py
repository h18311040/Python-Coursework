class Book:
    def __init__(self, book_id: int, name: str, author: str, publisher: str, rack_No: int):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.publisher = publisher
        self.rack_No = rack_No

    # DISPLAYS INFO ABOUT BOOK
    def display(self):
        print(f"Book_ID: {self.book_id} || Name: {self.name} || Author: {self.author} || "
              f"Publisher: {self.publisher} || Rack_No: {self.rack_No}")

    # UPDATES rack_No OF BOOK
    def update(self, var):
        self.rack_No = var
