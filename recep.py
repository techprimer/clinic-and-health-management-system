from tkinter import *
import mysql.connector
from tkinter import messagebox
import importlib

class doctor:

    def login(self):
        self.user = self.user_ent.get()
        self.passwd = self.pass_ent.get()

        mydb = mysql.connector.connect(host='127.0.0.1', user='root', db='hospital')
        mycursor = mydb.cursor()
        query = "select * from doctor where username=%s and password=%s"
        data = mycursor.execute(query, (self.user, self.passwd))
        if (len(mycursor.fetchall()) > 0):
            msg = messagebox.showinfo('DOCTOR LOGIN', 'you are logged in succesfully')



        else:
            msg = messagebox.showwarning('DOCTOR LOGIN', 'please enter valid username and password')


    def cancel(self):
        msg1 = messagebox.askyesno('doctor login', 'are you sure you want to exit from login')
        if (msg1):

            root.withdraw()
            importlib.import_module("loginas")




    def __init__(self, master):
        self.master = master

        self.f1 = Frame(master, width=1550, height=800, bg='#52a9ff')
        self.f1.pack()

        self.c1 = Canvas(self.f1, width=1550, height=800)
        self.photo1 = PhotoImage(master=self.c1, file='C:\\Users\\yash\\Desktop\\hos\\log1.gif')
        self.c1.create_image(0, 0, anchor=NW, image=self.photo1)
        self.c1.pack()


        self.label = Label(self.f1,text="LOGIN AS RECEPTIONIST",font="arial 12 bold",width=50,height=3,bg='#efff08')
        self.label.place(x=0,y=18)

        self.l1 = Label(self.f1, width=55, height=25, bg='#0fffd7')
        self.l1.place(x=610, y=70)

        self.l2 = Label(self.l1,width=25,height = 11,bg="blue")
        self.l2.place(x=80,y=15)
        self.c = Canvas(self.l2, width=225, height=225)
        self.photo = PhotoImage(master=self.c, file='C:\\Users\\yash\\Desktop\\hos\\doctor.gif')
        self.c.create_image(0, 0, anchor=NW, image=self.photo)
        self.c.pack()
        #self.c.create_oval(225, 225, 225, 225, fill="yellow",outline="black")


        self.f2 = Frame(master, width=393, height=400, bg='white')
        self.f2.place(x=610,y=340)

        self.userlabel = Label(self.f2,text="USERNAME  :-",font="arial 10 bold", width=25, height=2, bg='#0fffd7')
        self.userlabel.place(x=20, y=30)

        self.user_ent = Entry(self.f2, width=40, bg='lightgrey')
        self.user_ent.place(x=20, y=90,height=27)

        self.passlabel = Label(self.f2,text="PASSWORD :-",font="arial 10 bold", width=25, height=2, bg='#0fffd7')
        self.passlabel.place(x=20, y=160)

        self.pass_ent = Entry(self.f2,show='*', width=40, bg='lightgrey',)
        self.pass_ent.place(x=20, y=220, height=27)

        self.loginb = Button(self.f2, width=17, height=2, text='LOGIN', font='arial 10 bold',relief=RAISED,\
                         cursor="hand2", fg='black',bg='#00bbff')
        self.loginb.place(x=180, y=300)
        self.loginb.configure(command=self.login)

        self.cancelb = Button(self.f2, width=17, height=2, text='CANCEL', font='arial 10 bold',relief=RAISED,\
                         cursor="hand2", fg='black', bg='red')
        self.cancelb.place(x=20, y=300)
        self.cancelb.configure(command=self.cancel)






root = Tk()
b = doctor(root)

width_val = root.winfo_screenwidth()
height_val = root.winfo_screenheight()

root.geometry('%dx%d+0+0' % (width_val, height_val))
root.title("Receptionist LOGIN")
root.iconbitmap(r'C:\\Users\\yash\\Downloads\\hospital.ico')
root.mainloop()

