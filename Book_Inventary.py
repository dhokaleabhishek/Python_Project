class BookCollection:
    books = {}
    def __int__(self):
        pass
    def add_Book(self):
        self.book_name = input("Enter Book Name :: ")
        self.quantity = int(input("Enter Book Quantity :: "))

        if self.book_name not in BookCollection.books.keys():
            BookCollection.books[self.book_name] = self.quantity
        else:
            BookCollection.books[self.book_name] += self.quantity

    def remove_Book(self):
        self.book_name = input("Enter Book Name :: ")

        if self.book_name not in BookCollection.books.keys():
            print("Book Not Found !!")
            return
        else:
            self.quantity = int(input("Enter Book Quantity :: "))
            if self.quantity == BookCollection.books[self.book_name]:
                del(BookCollection.books[self.book_name])
                print("Quantity 0 , So Book is Deleted From Collection !")
            elif self.quantity < BookCollection.books[self.book_name]:
                BookCollection.books[self.book_name] -= self.quantity
            else:
                print("---    Book Quantity Exceeded !! \n---    PLEASE CHECK !!!")
                return

    def Total_Books(self):
        print("Total Quantity Of Books Available In The Collection :: ",sum(BookCollection.books.values()))
    @classmethod
    def display_Book_Collection(cls):
        print("----------------  book Collections  ----------------")
        print(BookCollection.books)

b1 = BookCollection()
choice = 1
while choice != 0:
    print("---------------MENU---------------")
    print(" 1. Add Book \n 2. Remove Book  \n 3. View Book Collection  \n 4. Get Total Books  \n 0. Exit  ")

    choice = int(input("Enter Performing Task ::"))

    if choice == 1:
        b1.add_Book()
    elif choice == 2:
        b1.remove_Book()

    elif choice == 3:
        b1.display_Book_Collection()

    elif choice == 4:
        b1.Total_Books()

    elif choice == 0:
        print("--------------------  Exit  --------------------")
        print("--------------------  Thank You  --------------------")
        break
