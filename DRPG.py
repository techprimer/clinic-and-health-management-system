from tkinter import *
import tkinter as tk
from tkinter import Frame
import mysql.connector
import importlib
from tkinter import messagebox
from typing import List, Any

#import self as self
#from doctorpanl import drpage

mySQLConnection = mysql.connector.connect(host='localhost',database='hospital',user='root',password='root')

cursor = mySQLConnection.cursor()
class drpage:
    def sbox(self):

        self.search = self.Entry2.get()
        self.searchbox()
    frame: Frame

    def done(self):
        self.value3 = self.Entry1.get()
        self.value2 = self.Entry.get()
        self.value1 = self.Entry2.get()


        if (
                self.value1 == '' or self.value2 == '' or self.value3 == '' ):
            msg1 = messagebox.showinfo("warning", "please fill all the fields")
        else:
            #mydb = mysql.connector.connect(host='127.0.0.1', user='root', db='hospital')
           # mycursor = mydb.cursor()
            query = "INSERT INTO docpanel (id,prescription,diagnosis) VALUES (%s,%s,%s)"
            cursor.execute(query, (
            self.value1, self.value2, self.value3))

            msg2 = messagebox.showinfo("prescription", "you succesfully saved patient data")

    def logout(self):
        root.withdraw()

        importlib.import_module("login")

    def searchbox(self):
        try:
          sql_select_query = """select * from pat where name = %s"""
          cursor.execute(sql_select_query, (self.search,))
          record = cursor.fetchall()
          for row in record:
                    self.label1 = Label(height=3, width=50)
                    self.label1.place(x=60, y=250)
                    self.label1.config(text="ID      : " + str(row[0]))

                    self.label2=Label(height=3,width=50)
                    self.label2.place(x=60,y=315)
                    self.label2.config(text="NAME      :" +str(row[1]))

                    self.label3 = Label(height=3, width=50)
                    self.label3.place(x=60, y=380)
                    self.label3.config(text="AGE        :" + str(row[2]))


        except mysql.connector.Error as error:

                print("Failed to get record from database: {}".format(error))







    def __init__(self, master, top=None):
        self.content = None
        self.master = master
        var1 = StringVar()
        var2 = StringVar()

        self.frame = Frame(master, width=1550, height=800, bg="lightgreen")
        self.frame.pack()

        assert isinstance(top, object)
        self.Frame1 = tk.Frame(top)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=1265)
        self.c1 = Canvas(self.Frame1, width=1550, height=800)
        self.photo1 = PhotoImage(master=self.c1, file='the.gif')
        self.c1.create_image(0, 0, anchor=NW, image=self.photo1)
        self.c1.pack()

        self.Frame1.place(relx=0.008, rely=0.199, relheight=0.787, relwidth=0.981)

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=355)

        self.Frame2.place(relx=0.016, rely=0.117, relheight=0.32, relwidth=0.281)


        self.Label6 = tk.Label(self.Frame2)
        self.Label6.place(relx=0.423, rely=0.121, height=26, width=186)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")

        self.Label7 = tk.Label(self.Frame2)
        self.Label7.place(relx=0.394, rely=0.485, height=26, width=192)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")

        self.Label8 = tk.Label(self.Frame2)
        self.Label8.place(relx=0.394, rely=0.727, height=26, width=192)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.024, rely=0.039, height=26, width=117)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI Semibold} -size 9 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Patient's Name :''')

        self.Label9 = tk.Label(self.Frame1)
        self.Label9.place(relx=0.024, rely=0.485, height=26, width=71)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Segoe UI Semibold} -size 9 -weight bold")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Diagosis :''')

        self.Label9 = tk.Label(self.Frame1)
        self.Label9.place(relx=0.480, rely=0.100, height=26, width=71)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="yellow")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Segoe UI Semibold} -size 9 -weight bold")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''prescription :''')

        self.dia_content = tk.StringVar()
        self.Entry1 = tk.Entry(self.Frame1, textvariable=self.dia_content)
        self.Entry1.place(relx=0.087, rely=0.485, height=144, relwidth=0.209)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.119, rely=0.039, height=24, relwidth=0.114)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.245, rely=0.039, height=33, width=60)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI Semibold} -size 9 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Search''')
        self.Button1.configure(command=self.sbox)

        self.Entry = tk.Entry(self.Frame1)
        self.Entry.place(relx=0.550, rely=0.039, height=100, relwidth=0.150)
        self.Entry.configure(background="white")
        self.Entry.configure(disabledforeground="#a3a3a3")
        self.Entry.configure(font="TkFixedFont")
        self.Entry.configure(foreground="#000000")
        self.Entry.configure(highlightbackground="#d9d9d9")
        self.Entry.configure(highlightcolor="black")
        self.Entry.configure(insertbackground="black")
        self.Entry.configure(selectbackground="#c4c4c4")
        self.Entry.configure(selectforeground="black")










        self.Button4 = tk.Button(self.Frame1, text="Done")
        self.Button4.place(relx=0.580, rely=0.485, height=63, width=106)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#2196f3")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Segoe UI Semibold} -size 13 -weight bold")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Done''')
        self.Button4.configure(command = self.done)
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.38, rely=0.015, height=46, width=312)
        self.Label1.configure(activebackground="lightgreen")
        self.Label1.configure(activeforeground="#e1d9e2")
        self.Label1.configure(background="lightgreen")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Yu Gothic UI Semibold} -size 14 -weight bold -slant italic -underline 1")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Dr. Shruti Patel''')

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.915, rely=0.155, height=23, width=65)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(takefocus="0")
        self.Button5.configure(text='''Log Out''')
        self.Button5.configure(width=65)
        self.Button5.configure(command=self.logout)

        self.label = Label(master, width=2, height=2, bg="black")
        self.label.place(x=1395, y=2)
        self.c2 = Canvas(self.label, width=100, height=100)
        self.photo2 = PhotoImage(master=self.c1, file='d.gif')
        self.c2.create_image(0, 0, anchor=NW, image=self.photo2)
        self.c2.pack()

    @staticmethod
    def popup2(event):
        Popupmenu2 = tk.Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#f9f9f9")
        Popupmenu2.configure(activeborderwidth="1")
        Popupmenu2.configure(activeforeground="black")
        Popupmenu2.configure(background="#d9d9d9")
        Popupmenu2.configure(borderwidth="1")
        Popupmenu2.configure(disabledforeground="#a3a3a3")
        Popupmenu2.configure(font="-family {Segoe UI} -size 9")
        Popupmenu2.configure(foreground="black")
        Popupmenu2.post(event.x_root, event.y_root)


def popup1(event, *args, **kwargs):
    Popupmenu1 = tk.Menu(root, tearoff=0)
    Popupmenu1.configure(activebackground="#f9f9f9")
    Popupmenu1.configure(activeborderwidth="1")
    Popupmenu1.configure(activeforeground="black")
    Popupmenu1.configure(background="#d9d9d9")
    Popupmenu1.configure(borderwidth="1")
    Popupmenu1.configure(disabledforeground="#a3a3a3")
    Popupmenu1.configure(font="-family {Segoe UI} -size 9")
    Popupmenu1.configure(foreground="black")
    Popupmenu1.post(event.x_root, event.y_root)


root = Tk()
b = drpage(root)
root.title("doctor panel")
root.iconbitmap('hospital.ico')
root.mainloop()
