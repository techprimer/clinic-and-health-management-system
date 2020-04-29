from tkinter import *
from tkinter import messagebox
#import mysql.connector
import importlib
class mainpage:

    def doctor(self):
        root.withdraw()
        #from py._builtin import execfile
        #execfile('recep.py')
        importlib.import_module("login")


        try:
            pass
        except:
            pass
    def rec(self):

        root.withdraw()
        importlib.import_module("recep")

        try:
            pass
        except:
            pass






    def __init__(self, master):
        self.master = master

        self.f1 = Frame(master, width=1550, height=800, bg='lightgreen')
        self.f1.pack()

        self.c = Canvas(self.f1, width=1550, height=800)
        self.photo = PhotoImage(master=self.c, file='C:\\Users\\yash\\Downloads\\pybackg.gif')
        self.c.create_image(0, 0, anchor=NW, image=self.photo)
        self.c.pack()

        self.l1 = Label(self.f1, text='NEWLIFE CLINIC AND HEALTH CENTRE', font=('segoeui 32 bold'), fg='red', bg='#0fffd7', width=70,
                        height=3)
        self.l1.place(x=0, y=50)

        self.l2 = Label(self.f1, width=16, height=16, bg='#0fffd7')
        self.l2.place(x=0, y=5)
        self.c1 = Canvas(self.l2, width=225, height=225)
        self.photo1 = PhotoImage(master=self.c, file='C:\\Users\\yash\\Desktop\\hos\\hosbuilding1.gif')
        self.c1.create_image(0, 0, anchor=NW, image=self.photo1)
        self.c1.pack()

        self.l3 = Label(self.f1, width=30, height=16, bg='black')
        self.l3.place(x=450, y=350)
        self.c2 = Canvas(self.l3, width=225, height=225)
        self.photo2 = PhotoImage(master=self.c2, file='C:\\Users\\yash\\Desktop\\hos\\docavtar.gif')
        self.c2.create_image(0, 0, anchor=NW, image=self.photo2)
        self.c2.pack()

        self.l4 = Label(self.f1, width=30, height=16, bg='black')
        self.l4.place(x=800, y=350)
        self.c3 = Canvas(self.l4, width=225, height=225)
        self.photo3 = PhotoImage(master=self.c3, file='C:\\Users\\yash\\Desktop\\hos\\receptionist.gif')
        self.c3.create_image(0, 0, anchor=NW, image=self.photo3)
        self.c3.pack()

        self.doctorb = Button(self.f1, width=23, height=2, text='DOCTOR',  relief=RAISED,\
                         cursor="hand2",font='arial 11 bold', fg='black',
                              bg='#2196f3')
        self.doctorb.place(x=450, y=650)
        self.doctorb.configure(command=self.doctor)


        self.receptionistb = Button(self.f1, width=23, height=2, text='RECEPTIONIST', relief=RAISED,\
                         cursor="hand2",font='arial 11 bold', fg='black',
                                    bg='#2196f3')
        self.receptionistb.place(x=800, y=650)
        self.receptionistb.configure(command=self.rec)

    # self.adminb = Button(self.f1, width=23, height=2, text='ADMIN', font='arial 11 bold', fg='black', bg='#2196f3')
    # self.adminb.place(x=1100, y=650)


root = Tk()
b = mainpage(root)

width_val = root.winfo_screenwidth()
height_val = root.winfo_screenheight()

root.geometry('%dx%d+0+0' % (width_val, height_val))
root.title("LOGIN AS")
root.iconbitmap(r'C:\\Users\\yash\\Downloads\\hospital.ico')

root.mainloop()