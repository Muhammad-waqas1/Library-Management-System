# Write a library class with no_of_books and books as two instance variables. Write a program to create a library form this library class and show how you can print all books, add a book and get the number of books uisng different methods. Show that your program doesnt persist the books after the program is stopped!

class library:
    def __init__(self,no_of_books,num_of_books,total_books):
        self.name=no_of_books
        self.num=num_of_books
        self.total=[]
    def show(self):
        # if(self.num+1!=len(self.name)):
        #     print("You gone mad !!")
        # libraring=[self.total]
        x=self.total.append(self.name)
        print(f"Number of books in Library {self.num}. Last book added was \"{self.name}\" .\n")
        # \nLibrary Now contains the following books:{libraring}\n")
        if(getting_books=="v"):
            print(f"Library contains following Books: \n")    
            for total in self.total:
                print(total)


    @property
    def add_books(self):
        return self.name
    @add_books.setter
    def add_books(self,new_value):
        self.name=new_value

    @property
    def num_books(self):
        return self.num
    @num_books.setter
    def num_books(self,num_of_books):
        self.num=num_of_books

    @property
    def total_books(self):
        return self.total
    @total_books.setter
    def total_books(self,num_of_books):
        self.total=num_of_books
        
newbooks=[]
a=library(len(newbooks),newbooks,len(newbooks))
for i in range(1,51):
    # print(i)
    getting_books=input("Press o to quit :: v to View all books in library\nAdd a book to the library:   ")
    # x=[]
    # x=x.append(getting_books)
    a.add_books=getting_books
    a.num_books=i
    a.show()
    booking=[]
    booking.append(getting_books)
    if(i==40):
        print("\nNote: You are approching to the limit.\nMessage: You can add only 50 books in the library.\n")
    elif(getting_books=="o"):
        break
    # elif(getting_books=="v"):
    #     print(f"Library contains following Books: \n")    
    #     for total in booking:
    #         print(total)

    elif(i==50):
        print("\nLibrary is FULL:")
    # print(a.add_books)

# a.add_books=12           #  The new value is setted to setter(add_books)
# # print(a.valuegain)
# print(a.add_books)           # Will became a **Getter**
# a.show()
    