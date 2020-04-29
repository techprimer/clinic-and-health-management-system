#import modules
from tkinter import *
import random
from tkinter import messagebox

# creating the object
root = Tk()

# resolution of the window
root.geometry("500x540+500+100")
root.title ("ABC HOSPITAL")
root.iconbitmap('hospital.ico')

# preventing the resize feature
root.resizable(False, False)

#Background Picture
photo1 = PhotoImage(file='back.png')
pic = Label(font=('arial' , 1 , 'bold'), image= photo1)
pic.place(x=0, y=0)

#LABELS=====================================================
heading = Label(font=('times new roman' , 25 , 'bold'), text="WELCOME TO ABC HOSPITAL", fg='black', bg='#fbf9d3')
heading.place(x=3, y=10)

heading = Label(font=('times new roman' , 22 , 'bold'), text="Choose Login", fg='black', bg='#fbf9d3')
heading.place(x=150, y=250)
#button to perform a command=======================================================
login = Button(font=('arial' , 20 , 'bold'),bd=14, text="DOCTOR's LOGIN", fg='white',bg='#04062c',width=27,height=2)
login.place(x=4,y=300)

login = Button(font=('arial' , 20 , 'bold'),bd=14, text="RECEPTION's LOGIN", fg='white',bg='#04062c',width=27,height=2)
login.place(x=4, y=420)
 
# end the loop********* DO NOT TOUCH***********                                    
root.mainloop()                             

