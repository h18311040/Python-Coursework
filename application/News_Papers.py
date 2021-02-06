from Book import Book


class News_Papers(Book):
    def __init__(self, book_id: int, name: str, author: str, publisher: str, rack_No: int, pages: int):
        super().__init__(book_id, name, author, publisher, rack_No)
        self.pages = pages

    # RETURNS PAGES
    def getPages(self):
        return self.pages