from tkinter import*
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Health Management System")

Tops=Frame(root, width=1600)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('helvetica',50,'bold'),text="PRESCRIPTION ",fg="Black",anchor="w")
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",anchor="w")
lblInfo.grid(row=1,column=0)

def Ref():
    
    if (Name.get()==""):
        CoName=0
    else:
        CoName=float(Name.get())


    
    if (Age.get()==""):
        CoAge=0
    else:
        CoAge=float(Age.get())



    if (Sex.get()==""):
        CoSex=0
    else:
        CoSex=float(Sex.get())



    if (Address.get()==""):
        CoAddress=0
    else:
        CoAddress=float(Address.get())

        
    if (Mobile.get()==""):
        CoMobile=0
    else:
        CoMobile=float(Mobile.get())

def qExit():
    root.destroy()

def Reset():
    
    Name.set("")
    Age.set("")
    Sex.set("")
    Address.set("")
    Mobile.set("")
    
#====================================Restaraunt Info 1===========================================================

Name=StringVar()
Age=StringVar()
Sex=StringVar()
Address=StringVar()
Mobile=StringVar()




lblName= Label(f1, font=('arial', 16, 'bold'),text="Name",bd=16,anchor="w")
lblName.grid(row=1, column=0)
txtName=Entry(f1, font=('arial',16,'bold'),textvariable=Name,bd=10,insertwidth=4,bg="Snow",justify='center')
txtName.grid(row=1,column=1)


lblAge= Label(f1, font=('arial', 16, 'bold'),text="Age",bd=16,anchor="w")
lblAge.grid(row=1, column=2)
txtAge=Entry(f1, font=('arial',16,'bold'),textvariable=Age,bd=10,insertwidth=4,bg="Snow",justify='center')
txtAge.grid(row=1,column=3)


lblSex= Label(f1, font=('arial', 16, 'bold'),text="Sex",bd=16,anchor="w")
lblSex.grid(row=3, column=0)
txtSex=Entry(f1, font=('arial',16,'bold'),textvariable=Sex,bd=10,insertwidth=4,bg="Snow",justify='center')
txtSex.grid(row=3,column=1)

lblMobile= Label(f1, font=('arial', 16, 'bold'),text="Mobile No",bd=16,anchor="w")
lblMobile.grid(row=3, column=2)
txtMobile=Entry(f1, font=('arial',16,'bold'),textvariable=Mobile,bd=10,insertwidth=4,bg="Snow",justify='center')
txtMobile.grid(row=3,column=3)

lblAddress= Label(f1, font=('arial', 16, 'bold'),text="Address",bd=16,anchor="w")
lblAddress.grid(row=5, column=0)
txtAddress=Entry(f1, font=('arial',16,'bold'),textvariable=Address,bd=10,insertwidth=4,bg="Snow",justify='center')
txtAddress.grid(row=5,column=1)



#==========================================Buttons==========================================================================================

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=1)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)


root.mainloop()


