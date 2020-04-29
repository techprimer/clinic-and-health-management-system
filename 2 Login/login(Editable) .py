#import modules
from tkinter import *
import mysql.connector
from mysql.connector import errorcode
import random
from tkinter import messagebox

# creating the object
root = Tk()

# resolution of the window
root.geometry("1520x790+0+0")
root.title ("ABC HOSPITAL")
root.iconbitmap('hospital.ico')

# preventing the resize feature
root.resizable(False, False)

# connect to the databse.
mySQLConnection = mysql.connector.connect(host='localhost',database='hospital',user='root',password='12345')
cursor = mySQLConnection.cursor(prepared=True)

#tkinter window
class Application:
    
#funtion to call when the SUBMIT BUTTON is clicked==========================================================================================================================================
    def login(self):
        # getting the user inputs
        self.val1 = self.username_ent.get()
        self.val2 = self.password_ent.get()
    
        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '':
            messagebox.showinfo("Warning", "Please Enter Your Credentials")
            
        # now we add to the database
        else:
            sql_select_query = """select * from login where userid=%s and pass=%s"""
            cursor.execute(sql_select_query, (self.val1,self.val2))
            record = cursor.fetchall()
        
            if (len(record) > 0):
                messagebox.showinfo('LOGIN' ,'Welcome ' +str(self.val1)+'  You Are Successfully Logged In')
            else:
                messagebox.showwarning('LOGIN' ,'Username ' +str(self.val1)+' Not Found OR Enter Valid Username & Password')    

#funtion for main frames=====================================================================================================================================================================

    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width= 1600, height= 900, bg='lightblue',relief=SUNKEN)
        self.left.pack(side=TOP)

        #Background Picture
        self.photo1 = PhotoImage(file='background.png')
        self.pic = Label(self.left, font=('arial' , 1 , 'bold'), image= self.photo1)
        self.pic.place(x=0, y=0)
        

#LABELS=====================================================
        self.heading = Label(self.left,font=('arial' , 50 , 'bold'), text="ABC Hospital", fg='black', bg='#06378b' ,anchor='w')
        self.heading.place(x=550, y=0)

        #Login Picture
        self.photo = PhotoImage(file= 'login.png')
        self.pic = Label(self.left, font=('arial' , 40 , 'bold'), image= self.photo ,fg = "lightblue", bg='#06378b')
        self.pic.place(x=640, y=100)
        
        # user name
        self.username = Label(self.left, text="Username", font=('arial 30 bold'), fg='black', bg='#063998')
        self.username.place(x=550, y=350)

        # password
        self.password = Label(self.left, text="Password", font=('arial 30 bold'), fg='black', bg='#063998')
        self.password.place(x=550, y=410)

#TEXTBOX=====================================================
        #username
        self.username_ent = Entry(self.left,font=('arial' , 20 , 'bold'))
        self.username_ent.place(x=750, y=360)
        
        #password
        self.password_ent = Entry(self.left, font=('arial' , 20 , 'bold'),show='*')
        self.password_ent.place(x=750, y=420)

# button to perform a command================================
        #button1
        self.login = Button(self.left,font=('arial' , 20 , 'bold'), text="LOGIN", bg='steelblue',command=self.login)
        self.login.place(x=700, y=480)
        

# end the loop********* DO NOT TOUCH***********
b = Application(root)                       #**
root.mainloop()                             #**
#******** DO NOT TOUCH*************************
