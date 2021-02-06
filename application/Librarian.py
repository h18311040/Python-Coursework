from Non_Teaching_Staff import Non_Teaching_Staff
from Student import Student
from Teaching_Staff import Teaching_Staff


class Librarian:
    def __init__(self, name: str, address: str, members=None):
        self.name = name
        self.address = address
        if members is None:
            self.members = []
        else:
            self.members = members

    # REGISTERS A MEMBER IN THE SYSTEM (MAKES AN OBJECT INSTANCE)
    def member_registration(self, type):
        if type == "Student" or type == "Teaching_Staff" or type == "Non_Teaching_Staff":
            member_id = int(input("Enter MemberID: "))
            name = input("Enter Name: ")
            branch = input("Enter Branch: ")
            address = input("Enter Address (City, Street): ")

            if type == "Student":
                year = int(input("Enter Year of study: "))
                roll_no = int(input("Enter Roll_No: "))
                student = Student(member_id, name, branch, address, year, roll_no)
                self.members.append(student)
                return student

            designation = input("Enter Designation: ")
            if type == "Teaching_Staff":
                teachingStaff = Teaching_Staff(member_id, name, branch, address, designation)
                self.members.append(teachingStaff)
                return teachingStaff

            elif type == "Non_Teaching_Staff":
                nonteachingStaff = Non_Teaching_Staff(member_id, name, branch, address, designation)
                self.members.append(nonteachingStaff)
                return nonteachingStaff

        else:
            print("Type is invalid!")

    # PRINTS ALL THE REGISTERED MEMBERS
    def print_members(self):
        for member in self.members:
            print(f"Member_ID: {member.member_id} || Name: {member.name} ||"
                  f" Branch: {member.branch} || Member_Type: {type(member).__name__}")

    # PRINTS INFO ABOUT SELF
    def info(self):
        print(f"Name: {self.name} || Address: {self.address} || Member count: {len(self.members)}")
