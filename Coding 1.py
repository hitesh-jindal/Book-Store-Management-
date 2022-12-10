import pandas as pd
import matplotlib.pyplot as plt


print("---------- WELCOME TO JINDAL BOOK STORE ----------")

def addNewBook():
    bookid= int(input("Enter the book id: "))
    title= input("Enter book title: ")
    author= input("Enter author of the book ")
    publisher= input("Enter book publisher")
    edition= input("Enter edition of the book ")
    cost= int(input("Enter cost of the book "))
    category= input("Enter category of the book ")
    bdf= pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Books.csv")
    n= bdf["bookid"].count()
    bdf.at[n]= [bookid,title,author,publisher,edition,cost,category]
    bdf.to_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Books.csv",index=False)
    print("Book added successfully")
    print(bdf)



def searchBook():
    title= input("Enter book title: ")
    bdf=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Books.csv")
    df=bdf.loc[bdf["title"]==title]
    if df.empty:
        print("No book found with given code")
    else:
        print("Books details are:")
        print(df)


def deleteBook():
    bookid= float(input("Enter the bood id: "))
    bdf=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Books.csv")
    bdf=bdf.drop(bdf[bdf["bookid"]== bookid].index)
    bdf.to_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Books.csv", index=False)
    print("Book Deleted Successfully")
    print(bdf)


def showBooks():
    bdf=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Books.csv")
    print(bdf)


def addNewEmployee():
    eid= int(input("Enter the employee id: "))
    e_name= input("Enter the Employee Name: ")
    phoneno= int(input("Enter phone number"))
    doj= input("Enter Date of Joining")
    edf= pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Employee.csv")
    n= edf["eid"].count()
    edf.at[n]= [eid,e_name,phoneno,doj]
    edf.to_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Employee.csv")
    print("New Member added successfully")
    print(edf)



def searchEmployee():
    e_name= input("Enter a employee name: ")
    bdf=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Employee.csv")
    df= bdf.loc[bdf["e_name"]==e_name]
    if df.empty:
        print("No Employee found with the given name")
    else:
        print("Members details are")
        print(df)
 
        
def deleteEmployee():
    eid= float(input("Enter a employee id"))
    bdf=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Employee.csv")
    bdf=bdf.drop(bdf[bdf["eid"]==eid].index)
    bdf.to_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Employee.csv", index=False)
    print("Employee Deleted successfully")
    print(bdf)

def showEmployes():
    bdf=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Employee.csv")
    print(bdf)

def saleBook():
    book_name= input("Enter book name : ")
    bdf=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Books.csv")
    df= bdf.loc[bdf["title"]==book_name]
    if df.empty:
        print("No Book found in the store")
        return

    e_name= input("Enter employee name: ")
    edf= pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Employee.csv")
    edf=edf.loc[edf["e_name"]==e_name]
    if edf.empty:
        print("No such employee found")
        return

    dateofsale= input("Enter the date: ")
    qty= int(input("Enter number of books sold: "))
    bdf=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Sale.csv")
    n= bdf["book_name"].count()
    bdf.at[n]= [book_name,e_name,dateofsale,qty]
    bdf.to_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Sale.csv", index= False)
    print("Book Sold")
    print(bdf)

def showsoldBooks():
    idf=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Sale.csv")
    print(idf)

def deletesoldBooks():
    book_name= input("Enter book name: ")
    bdf=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Sale.csv")
    bdf=bdf.drop(bdf[bdf["book_name"]==book_name].index)
    bdf.to_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Sale.csv", index= False)
    print("Deleted sold book successfully")
    print(bdf)

def showCharts():
    print("Press1 - Books and their cost")
    print("Press2 - Number of Books sold by employes ")
    ch= int(input("Enter your Choice: "))
    if ch==1:
        df=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Books.csv")
        df= df[["title","cost"]]
        df.plot("title","cost",kind='bar')
        plt.xlabel('title------>')
        plt.ylabel('cost------>')
        plt.show()
        return

    elif ch==2:
        df=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Sale.csv")
        df=df[["qty","e_name"]]
        df.plot(kind='bar', color="red")
        plt.show()


def login():
    uname= input("Enter Username : ")
    pwd= input("Enter Password : ")
    df=pd.read_csv(r"C:\Users\akshay\Documents\XII Hitesh\Informatics Practices\Project Book store\Users.csv")
    df= df.loc[df["uname"]== uname]
    if df.empty:
        print("Invalid Username given")
        return False
    else:
        df= df.loc[df["pwd"]== pwd]
        if df.empty:
            print("Invalid Password")
            return False
        else:
            print("Username and password matched successfully")
            return True

def showMenu():
    print("---------------------------------------------------------")
    print("              JINDAL BOOK STORE                          ")
    print("---------------------------------------------------------")
    print("Press 1- Add a New Book")
    print("Press 2- Search for a Book")
    print("Press 3- Delete a Book")
    print("Press 4- Show all Books")
    print("Press 5- Add a New Employee")
    print("Press 6- Search for a Employee")
    print("Press 7- Delete a Employee")
    print("Press 8- Show all Employes")
    print("Press 9- Sell a book")
    print("Press 10- Show all sold book")
    print("Press 11- Delete a sold book")
    print("Press 12- To view Charts")
    print("Press 13- To exit")
    choice= int(input("Enter your choice : "))
    return choice
if login():
    while True:
        ch= showMenu()
        if ch==1:
            addNewBook()
        elif ch==2:
            searchBook()
        elif ch==3:
            deleteBook()
        elif ch==4:
            showBooks()
        elif ch==5:
            addNewEmployee()
        elif ch==6:
            searchEmployee()
        elif ch==7:
            deleteEmployee()
        elif ch==8:
            showEmployes()
        elif ch==9:
            saleBook()
        elif ch==10:
            showsoldBooks()
        elif ch==11:
            deletesoldBooks()
        elif ch==12:
            showCharts()
        elif ch==13:
            break
        else:
            print("Invalid Option Selected")

print("THANKYOU FOR VISITING OUR STORE")
    
