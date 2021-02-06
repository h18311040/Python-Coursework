from Member import Member


class Non_Teaching_Staff(Member):
    def __init__(self, member_id: int, name: str, branch: str, address: str, designation: str):
        super().__init__(member_id, name, branch, address, books=None)
        self.designation = designation

    # RETURNS DESIGNATION
    def getDesignation(self):
        return self.designation
