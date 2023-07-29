# STUDENT LIBRABRY
class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks

    def displayavailabelbooks(self):
        print("books present in this library are: ")
        for book in self.books:
            print( "\t *"   + book) 

    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname} .Please keep it safely and return it within 30 days ") 
            self.books.remove(bookname)
            return True
        else:
            print("sorrry, this book has not available currently. Please wait untill the book is returned")
            return False
        
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning the books")



class Student:
    def requestbook(self):
        self.book =input("Enter the name of the book you want to borrow")
        return self.book

    


    def returnbook(self):
        self.book =input("Enter the name of the book you want to return")
        return self.book

    

if __name__ == "__main__":
    CentralLibrary = Library(["DSA" ,"PYTHON", "DJANGO" ,"JAVA" ,"C++"])
    Student = Student()

    while(True):
        welcome = '''=====Welcome to the CentralLibrabry=====
        please choose an option: 
        1. List the books 
        2. Request the books
        3. Return the books
        4. Exit the Librabry'''

        print(welcome)  

        a = int(input("Enter a choice: "))
        if a == 1:
            CentralLibrary.displayavailabelbooks()
        elif a == 2:
            CentralLibrary.borrowbook()
        elif a == 3:
            CentralLibrary.returnbook()
        elif a == 4:
            print("Thanks for visiting Librabry")
            exit()
        else:
            print("Invalid choice")            

          



     