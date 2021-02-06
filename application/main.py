# SVETOSLAV ZHEKOV F-NUM: 18311040
from Journals import Journals
from Librarian import Librarian
from Magazines import Magazines
from News_Papers import News_Papers
from Reference_Books import Reference_Books
from Student import Student
import time

# LIBRARIAN
print("---------------------------LIBRARIAN--------------------------")
librarian1 = Librarian("Steve", "Burgas, Slaveikov")
librarian1.info()

print("\n")
# ALL BOOKS
book1 = Magazines(1, "Dark Ages", "Steven O'Donald", "Book Enterprise", 1, 5, 1999)
book2 = Journals(2, "Venomous", "Mat Harold", "Publicise", 2, 10)
book3 = News_Papers(3, "New York Times", "NYT", "New York Times", 3, 25)
book4 = Reference_Books(4, "Retribution", "Alan Beck", "fantasy Books", 4, 1, "BG1234RAB1533")
book5 = Journals(5, "Islands", "Mat Harold", "Publicise", 2, 10)
book6 = Magazines(6, "21-st Century", "Steven O'Donald", "Book Enterprise", 1, 2, 2002)

# THE BOOK LIST
books = [book1, book2, book3, book4, book5, book6]

# A COUPLE OF MEMBERS
student = Student(1, "Sam", "IT", "Burgas, Slaveikov", 3, 4)
student1 = Student(2, "Bob", "IT", "Sofia, Vuzrajdane", 4, 5)
librarian1.members.append(student)
librarian1.members.append(student1)


# MENU INTERFACE
def menu():
    print("---------------------------ALL POSSIBLE CHOICES--------------------------")
    print("1.Register a member (Student, Teaching_Staff, Non_Teaching_Staff).")
    print("2.Print all registered members.")
    print("3.Member requests a book.")
    print("4.Member returns a book.")
    print("5.Print all books that a member has.")
    print("6.Print all info about the Librarian.")
    print("7.Print all the available books.")
    print("8.Update rack_No of a book.")
    print("9.Exit Menu.")


def printBooklist():
    for book in books:
        print(f"Book_ID: {book.book_id} || Name: {book.name} || Type: {type(book).__name__} || Rack_No: {book.rack_No}")


def choice1():
    typeMember = input(
        "You selected choice 1, put in a type for the member (Student, Teaching_Staff, Non_Teaching_Staff): ")
    librarian1.member_registration(typeMember)


def choice2():
    print("You selected choice 2, printing all registered members: ")
    librarian1.print_members()


def choice3():
    librarian1.print_members()
    print("\n")
    idMember = int(input("You selected choice 3, put in the Member_ID of the member which requests the book: "))

    for member in librarian1.members:
        if idMember == member.member_id:
            print("\n")
            printBooklist()
            print("\n")
            idBook = int(input("Put in the Book_ID of the book wanted: "))

            for book in books:
                if idBook == book.book_id:
                    member.books.append(book)
                    books.remove(book)


def choice4():
    librarian1.print_members()
    print("\n")
    idMember = int(input("You selected choice 4, put in the Member_ID of the member which returns the book: "))

    for member in librarian1.members:
        if idMember == member.member_id:
            print("\n")
            for book in member.books:
                print(f"Book_ID: {book.book_id} || Name: {book.name} ||"
                      f" Type: {type(book).__name__} || Rack_No: {book.rack_No}")
            print("\n")
            idBook = int(input("Put in the Book_ID of the book which needs to be returned: "))

            for book in member.books:
                if idBook == book.book_id:
                    member.books.remove(book)
                    books.append(book)


def choice5():
    librarian1.print_members()
    print("\n")
    idMember = int(input("You selected choice 5, enter Member_ID to print all the books he/she has: "))
    for member in librarian1.members:
        if idMember == member.member_id:
            member.books_in_possession()
            break


def choice6():
    print("You selected choice 6, printing information about the Librarian: ")
    librarian1.info()


def choice7():
    print("You selected choice 7, printing all available books: ")
    printBooklist()


def choice8():
    printBooklist()
    idBook = int(input("You selected choice 8, enter the Book_ID of the book which you want to update the rack_No: "))
    rack_No = int(input("Enter the new rack_No: "))
    for book in books:
        if idBook == book.book_id:
            book.rack_No = rack_No


menu()
print("\n")
choice = int(input("Enter your choice: "))

# A SLEEP TIMER SO INFORMATION IS SEEN WHEN IT SHOWS IN CONSOLE
sleepTime = 1

while choice != 9:

    if choice == 1:
        choice1()
        time.sleep(sleepTime)

    elif choice == 2:
        choice2()
        time.sleep(sleepTime)

    elif choice == 3:
        choice3()
        time.sleep(sleepTime)

    elif choice == 4:
        choice4()
        time.sleep(sleepTime)

    elif choice == 5:
        choice5()
        time.sleep(sleepTime)

    elif choice == 6:
        choice6()
        time.sleep(sleepTime)

    elif choice == 7:
        choice7()
        time.sleep(sleepTime)

    elif choice == 8:
        choice8()
        time.sleep(sleepTime)
    else:
        print("Incorrect choice!")

    print("\n")
    menu()
    print("\n")
    choice = int(input("Enter your choice: "))

print("\n")
print("You have exited the program!")