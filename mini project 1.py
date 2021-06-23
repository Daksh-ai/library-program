'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''



class lib:
    def __init__(self,name):
        self.name=name
        self.li=["let us c","let us python","coding"]
    def display(self):
        return self.li
    def booklend(self):
        a=input("enter the book name")
        return "BOOK OWN,CONGRATULATION!!"
        for i in range(2):
            if a==self.li[i]:
                self.li.remove(a)
    def add_book(self,aname):
        b=input("Enter book you donate")
        self.aname=aname
        self.li.append(b)
        print("THANKS FOR DONATE")
        return "the book is doante by {}:".format(self.aname)
    def return_book(self,p):
        self.p=p
        c=input("Enter the book name")
        for i in range(3):
            if c==self.li[i]:
                print("the book is give by {} ".format(self.p))
                return "THANK YOU, VISIT AGAIN"
                
    
if __name__ == '__main__':
    m=lib(input("Enter the username:"))
    n=input("Enter the password")
    if len(n)>7:
        print("welcome")
    elif len(n)<7:
        print("most welcome")
    print("1:display Books of the library\n2:Book lend\n3:add book in library\n4:return book")
    x=int(input("Enter the following code"))
    if x==1:
        print(m.li)
    elif x==2:
        print(m.li)
        print(m.booklend())
    elif x==3:
        print(m.add_book(input("Enter The your Name:")))
    elif x==4:
        print(m.li)
        print(m.return_book(input("Enter the Name")))
    else:
        print("Error 404 found! ")


    

