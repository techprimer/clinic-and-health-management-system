from tkinter import*
import random
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

lblInfo=Label(Tops,font=('helvetica',50,'bold'),text="Billing System ",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Tomato",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

        
    if (Bed_charge.get()==""):
        CoBed_charge=0
    else:
        CoBed_charge=float(Bed_charge.get())


    if (Room_charge.get()==""):
        CoRoom_charge=0
    else:
        CoRoom_charge=float(Room_charge.get())


    if (Doctor_charge.get()==""):
        CoDoctor_charge=0
    else:
        CoDoctor_charge=float(Doctor_charge.get())

        
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

                   
    CostofDrinks=CoD
    CostofBed_charge = CoBed_charge
    CostofRoom_charge = CoRoom_charge
    CostDoctor_charge = CoDoctor_charge
    
    Costof= "Rs", str('%.2f' % (CostofDrinks+CostofBed_charge+CostofRoom_charge+CostDoctor_charge))

    PayTax=((CostofDrinks+CostofBed_charge+CostofRoom_charge+CostDoctor_charge) * 0.2)

    TotalCost=(CostofDrinks+CostofBed_charge+CostofRoom_charge+CostDoctor_charge)
 
    Ser_Charge= ((CostofDrinks+CostofBed_charge+CostofRoom_charge+CostDoctor_charge)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service) 
    Tax.set(PaidTax)
    SubTotal.set(Costof)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Bed_charge.set("")
    Room_charge.set("")
    Total.set("")
    SubTotal.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Doctor_charge.set("")
    
    
#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Bed_charge=StringVar()
Room_charge=StringVar()
Total=StringVar()
SubTotal=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Doctor_charge=StringVar()

lblDoctor_charge= Label(f1, font=('arial', 16, 'bold'),text="Doctor_charge",bd=16,anchor="w")
lblDoctor_charge.grid(row=1, column=0)
txtDoctor_charge=Entry(f1, font=('arial',16,'bold'),textvariable=Doctor_charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDoctor_charge.grid(row=1,column=1)

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Medicine Cost",bd=16,anchor="w")
lblDrinks.grid(row=4, column=0)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=4,column=1)

lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="Pale Green",justify='right')
txtReference.grid(row=0,column=1)

lblBed_charge= Label(f1, font=('arial', 16, 'bold'),text="Bed charge",bd=16,anchor="w")
lblBed_charge.grid(row=2, column=0)
txtBed_charge=Entry(f1, font=('arial',16,'bold'),textvariable=Bed_charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBed_charge.grid(row=2,column=1)


lblRoom_charge= Label(f1, font=('arial', 16, 'bold'),text="Room charge",bd=16,anchor="w")
lblRoom_charge.grid(row=3, column=0)
txtRoom_charge=Entry(f1, font=('arial',16,'bold'),textvariable=Room_charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtRoom_charge.grid(row=3,column=1)



#============================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================

lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=1, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="Pale Goldenrod",justify='right')
txtService.grid(row=1,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=2, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="Pale Goldenrod",justify='right')
txtStateTax.grid(row=2,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=3, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="Pale Goldenrod",justify='right')
txtSubTotal.grid(row=3,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=4, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="Pale Goldenrod",justify='right')
txtTotalCost.grid(row=4,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="Blue Violet",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="Blue Violet",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="Blue Violet",command=qExit).grid(row=7,column=3)


root.mainloop()


