import tkinter as tk
class Library:
    def __init__(self): # constructor method was created
        self.file=open("books.txt","a+")

    def __del__(self): # destructor method was created
        self.file.close()
    
    def listBooks(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        booksList = []
        for line in lines:
            bookInfo = line.split(',')
            booksList.append(bookInfo)

        if not booksList:
            print("No registration yet.")
        else:
            for book in booksList:
                print(f"Book Name: {book[0]}, Author: {book[1]}")

    def addBook(self):
        bookTitle = input("Enter the book title : ")
        bookAuthor = input("Enter the book author : ")
        releaseYear = input("Enter the release year : ")
        numPages = input("Enter number of pages : ")
        bookInfo =f"{bookTitle},{bookAuthor},{releaseYear},{numPages}\n"
        self.file.write(bookInfo)
        print("Book added successfully!")


    def removeBook(self):
        titleRemove =input("Enter the title ofthe book to remove: ")
        self.file.seek(0)
        lines =self.file.readlines()
        updatedLines = []
        for line in lines:
            if titleRemove not in line:
                updatedLines.append(line)
        self.file.seek(0)
        self.file.truncate(0)
        for line in updatedLines:
            self.file.write(line)
            print("Book removed successfully!")

lib =Library()


while True:

    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Exit")
    choice = input("Enter your choice (1/2/3/Q): ")

   
    if choice == "1":
        lib.listBooks()
    elif choice == "2":
        lib.addBook()
    elif choice == "3":
        lib.removeBook()
    elif choice.upper() == "Q":
        print("Exiting the program...")
        break  
    else:
        print("Invalid choice! Please enter 1, 2, 3 or Q.")



