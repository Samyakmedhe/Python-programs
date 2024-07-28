
class Booksstore():
    NoOfBooks = 0

    def __init__(self,name , Author):
        self.name = name
        self.Author = Author

        Booksstore.NoOfBooks += 1
    def Display(self):
        print("Name : ",self.name)
        print("Author name :",self.Author)
        print("No of books : ",Booksstore.NoOfBooks)


Obj1 = Booksstore("Linux System programing","Robert love")
Obj1.Display()

Obj2 = Booksstore("C programing","Dinnis Ritchie")
Obj2.Display()
