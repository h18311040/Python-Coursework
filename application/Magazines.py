from Book import Book


class Magazines(Book):
    def __init__(self, book_id: int, name: str, author: str, publisher: str, rack_No: int,  issue_No: int, year):
        super().__init__(book_id, name, author, publisher, rack_No)
        self.issue_No = issue_No
        self.year = year

    # RETURNS ISSUE_NO
    def getIssueNo(self):
        return self.issue_No

    # RETURNS YEAR
    def getYear(self):
        return self.year
