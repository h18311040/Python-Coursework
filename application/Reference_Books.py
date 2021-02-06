from Book import Book


class Reference_Books(Book):
    def __init__(self, book_id: int, name: str, author: str, publisher: str, rack_No: int, edition: int, isbn: str, ):
        super().__init__(book_id, name, author, publisher, rack_No)
        self.edition = edition
        self.isbn = isbn

    # RETURNS ISBN
    def getISBN(self):
        return self.isbn
