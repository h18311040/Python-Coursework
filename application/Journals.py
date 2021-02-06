from Book import Book


class Journals(Book):
    def __init__(self, book_id: int, name: str, author: str, publisher: str, rack_No: int, volume: int):
        super().__init__(book_id, name, author, publisher, rack_No)
        self.volume = volume

    # RETURNS VOLUME
    def getVolume(self):
        return self.volume
