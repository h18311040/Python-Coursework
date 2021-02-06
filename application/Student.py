from Member import Member


class Student(Member):
    def __init__(self, member_id: int, name: str, branch: str, address: str, year: int, roll_No: int):
        super().__init__(member_id, name, branch, address, books=None)
        self.year = year
        self.roll_No = roll_No

    # RETURNS YEAR
    def getYear(self):
        return self.year

    # RETURNS ROLL NUMBER
    def getRollNo(self):
        return self.roll_No
