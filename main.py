class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks
    
    def displayAvailableBooks(self):
        print("Books present at the Library are: \n")
        for book in self.books:
            print(f"{book} \n")

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"This book {bookName} has been issued to you, please return it before 30 days\n")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry, this book {bookName} has been issued to someone else!\n")
            return False
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"Thanks for returning the book {bookName}.\n")
    

class Student:
    def requestBook(self):
        self.book = input("Enter the book name that you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book name that you want to return: ")
        return self.book

if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()
    while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        5..................
        '''
        print(welcomeMsg)
        choiceOption = int(input("Enter a choice: "))
        if choiceOption == 1:
            centraLibrary.displayAvailableBooks()
        elif choiceOption == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif choiceOption == 3:
            centraLibrary.returnBook(student.returnBook())
        elif choiceOption == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
        

        