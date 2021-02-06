class Member:
    def __init__(self, member_id: int, name: str, branch: str, address: str, books=None):
        self.member_id = member_id
        self.name = name
        self.branch = branch
        self.address = address
        if books is None:
            self.books = []
        else:
            self.books = books

    # REQUESTS BOOK, IF BOOK IS NOT AVAILABLE, "You already have that book!" WILL PRINT
    def request_book(self, book: object):
        if book in self.books:
            print("You already have that book!")
        else:
            self.books.append(book)

    # RETURNS THE BOOK, TRANSACTION IS REMOVED FROM TRANSACTIONS LIST AND IS DESTROYED
    def return_book(self, book: object):
        if book in self.books:
            self.books.remove(book)
        else:
            print("You don't have the book!")

    # PRINTS ALL THE BOOKS YHE MEMBER HAS
    def books_in_possession(self):
        for book in self.books:
            print(f"Book_ID: {book.book_id} || Name: {book.name} || Type: {type(book).__name__}")
