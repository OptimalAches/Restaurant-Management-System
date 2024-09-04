import random 
import time
import datetime
import tkinter.messagebox
from tkinter import*

root=Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")
root.configure(background ='Cadet Blue')

Tops = Frame(root, bg='Cadet Blue', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('arial',60, 'bold'), text="Restaurant Management System", bd=21,bg='Cadet Blue',
                 fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)


ReceiptCal_F = Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame, bg='Powder blue', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Cake_F.pack(side=RIGHT)
#=========================================================Variables===================================================================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator =""

E_Tea=StringVar()
E_Coffee=StringVar()
E_Lassi=StringVar()
E_Pepsi=StringVar()
E_Coca_Cola=StringVar()
E_Masala_Soda=StringVar()
E_Milkshake=StringVar()
E_Virgin_Mojito=StringVar()

E_Chocolate_Cake=StringVar()
E_Vanilla_Cake=StringVar()
E_Strawberry_Cake=StringVar()
E_Butterscotch_Cake=StringVar()
E_Black_Forest_Cake=StringVar()
E_Red_Velvet_Cake=StringVar()
E_Caramel_Cake=StringVar()
E_Carrot_Cake=StringVar()

E_Tea.set("0")
E_Coffee.set("0")
E_Lassi.set("0")
E_Pepsi.set("0")
E_Coca_Cola.set("0")
E_Masala_Soda.set("0")
E_Milkshake.set("0")
E_Virgin_Mojito.set("0")

E_Chocolate_Cake.set("0")
E_Vanilla_Cake.set("0")
E_Strawberry_Cake.set("0")
E_Butterscotch_Cake.set("0")
E_Black_Forest_Cake.set("0")
E_Red_Velvet_Cake.set("0")
E_Caramel_Cake.set("0")
E_Carrot_Cake.set("0")


DateofOrder.set(time.strftime("%d/%m/%Y"))
#===================================================================================================================================
def iExit():
    iExit =tkinter.messagebox.askyesno("Exit Restaurant System", "confirm if you want to exit")
    if iExit > 0:
       root.destroy()
       return

def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0".END)


    E_Tea.set("0")
    E_Coffee.set("0")
    E_Lassi.set("0")
    E_Pepsi.set("0")
    E_Coca_Cola.set("0")
    E_Masala_Soda.set("0")
    E_Milkshake.set("0")
    E_Virgin_Mojito.set("0")


    E_Chocolate_Cake.set("0")
    E_Vanilla_Cake.set("0")
    E_Strawberry_Cake.set("0")
    E_Butterscotch_Cake.set("0")
    E_Black_Forest_Cake.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Caramel_Cake.set("0")
    E_Carrot_Cake.set("0")


    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtTea.configure(state =DISABLED)
    txtCoffee.configure(state =DISABLED)
    txtLassi.configure(state =DISABLED)
    txtPepsi.configure(state =DISABLED)
    txtCoca_Cola.configure(state =DISABLED)
    txtMasala_Soda.configure(state =DISABLED)
    txtMilkshake.configure(state =DISABLED)
    txtVirgin_Mojito.configure(state =DISABLED)
    txtChocolate_Cake.configure(state =DISABLED)
    txtVanilla_Cake.configure(state =DISABLED)
    txtStrawberry_Cake.configure(state =DISABLED)
    txtButterscotch_Cake.configure(state =DISABLED)
    txtBlack_Forest_Cake.configure(state =DISABLED)
    txtRed_Velvet_Cake.configure(state =DISABLED)
    txtCaramel_Cake.configure(state =DISABLED)
    txtCarrot_Cake.configure(state =DISABLED)

def CostofItem():
    Item1=float(E_Tea.get())
    Item2=float(E_Coffee.get())
    Item3=float(E_Lassi.get())
    Item4=float(E_Pepsi.get())
    Item5=float(E_Coca_Cola.get())
    Item6=float(E_Masala_Soda.get())
    Item7=float(E_Milkshake.get())
    Item8=float(E_Virgin_Mojito.get())

    Item9=float(E_Chocolate_Cake.get())
    Item10=float(E_Vanilla_Cake.get())
    Item11=float(E_Strawberry_Cake.get())
    Item12=float(E_Butterscotch_Cake.get())
    Item13=float(E_Black_Forest_Cake.get())
    Item14=float(E_Red_Velvet_Cake.get())
    Item15=float(E_Caramel_Cake.get())
    Item16=float(E_Carrot_Cake.get())

    PriceofDrinks =(Item1 * 20) + (Item2 * 25) + (Item3 * 30) \
                            + (Item4 * 50) + (Item5 * 50) + (Item6 * 40) + (Item7 * 70) + (Item8 * 60)
    
    PriceofCakes =(Item9 * 300) + (Item10 * 300) + (Item11* 350) \
                   +(Item12* 400) + (Item13* 420) + (Item14* 450) + (Item15* 500) + (Item16 * 550)

    DrinksPrice ='₹' '%.2f'%(PriceofDrinks)
    CakesPrice ='₹' '%.2f'%(PriceofCakes)
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice) 
    SC='₹' '%.2f'%(20)
    ServiceCharge.set(SC)

    SubTotalofITEMS ='₹' '%.2f'%(PriceofDrinks + PriceofCakes + 20)
    SubTotal.set(SubTotalofITEMS)

    Tax='₹' '%.2f'%((PriceofDrinks + PriceofCakes + 20)*0.05)
    PaidTax.set(Tax)
    TT =((PriceofDrinks + PriceofCakes + 20)*0.05)
    TC ='₹' '%.2f'%(PriceofDrinks + PriceofCakes + 20 + TT )
    TotalCost.set(TC)

def chkTea():
    if (var1.get() == 1):
        txtTea.configure(state = NORMAL)
        txtTea.focus()
        txtTea.delete('0', END)
        E_Tea.set("")
    elif(var1.get() == 0):
        txtTea.configure(state = DISABLED)
        E_Tea.set("0")
def chkCoffee():
    if (var2.get() == 1):
        txtCoffee.configure(state = NORMAL)
        txtCoffee.focus()
        txtCoffee.delete('0', END)
        E_Coffee.set("")
    elif(var2.get() == 0):
        txtCoffee.configure(state = DISABLED)
        E_Coffee.set("0")
def chkLassi():
    if (var3.get() == 1):
        txtLassi.configure(state = NORMAL)
        txtLassi.focus()
        txtLassi.delete('0', END)
        E_Lassi.set("")
    elif(var3.get() == 0):
        txtLassi.configure(state = DISABLED)
        E_Lassi.set("0")
def chkPepsi():
    if (var4.get() == 1):
        txtPepsi.configure(state = NORMAL)
        txtPepsi.focus()
        txtPepsi.delete('0', END)
        E_Pepsi.set("")
    elif(var4.get() == 0):
        txtPepsi.configure(state = DISABLED)
        E_Pepsi.set("0")
def chkCoca_Cola():
    if (var5.get() == 1):
        txtCoca_Cola.configure(state = NORMAL)
        txtCoca_Cola.focus()
        txtCoca_Cola.delete('0', END)
        E_Coca_Cola.set("")
    elif(var5.get() == 0):
        txtCoca_Cola.configure(state = DISABLED)
        E_Coca_Cola.set("0")
def chkMasala_Soda():
    if (var6.get() == 1):
        txtMasala_Soda.configure(state = NORMAL)
        txtMasala_Soda.focus()
        txtMasala_Soda.delete('0', END)
        E_Masala_Soda.set("")
    elif(var6.get() == 0):
        txtMasala_Soda.configure(state = DISABLED)
        E_Masala_Soda.set("0")
def chkMilkshake():
    if (var7.get() == 1):
        txtMilkshake.configure(state = NORMAL)
        txtMilkshake.focus()
        txtMilkshake.delete('0', END)
        E_Milkshake.set("")
    elif(var7.get() == 0):
        txtMilkshake.configure(state = DISABLED)
        E_Milkshake.set("0")
def chkVirgin_Mojito():
    if (var8.get() == 1):
        txtVirgin_Mojito.configure(state = NORMAL)
        txtVirgin_Mojito.focus()
        txtVirgin_Mojito.delete('0', END)
        E_Virgin_Mojito.set("")
    elif(var8.get() == 0):
        txtVirgin_Mojito.configure(state = DISABLED)
        E_Virgin_Mojito.set("0")
def chkChocolate_Cake():
    if (var9.get() == 1):
        txtChocolate_Cake.configure(state = NORMAL)
        txtChocolate_Cake.focus()
        txtChocolate_Cake.delete('0', END)
        E_Chocolate_Cake.set("")
    elif(var9.get() == 0):
        txtChocolate_Cake.configure(state = DISABLED)
        E_Chocolate_Cake.set("0")
def chkVanilla_Cake():
    if (var10.get() == 1):
        txtVanilla_Cake.configure(state = NORMAL)
        txtVanilla_Cake.focus()
        txtVanilla_Cake.delete('0', END)
        E_Vanilla_Cake.set("")
    elif(var10.get() == 0):
        txtVanilla_Cake.configure(state = DISABLED)
        E_Vanilla_Cake.set("0")
def chkStrawberry_Cake():
    if (var11.get() == 1):
        txtStrawberry_Cake.configure(state = NORMAL)
        txtStrawberry_Cake.focus()
        txtStrawberry_Cake.delete('0', END)
        E_Strawberry_Cake.set("")
    elif(var11.get() == 0):
        txtStrawberry_Cake.configure(state = DISABLED)
        E_Strawberry_Cake.set("0")
def chkButterscotch_Cake():
    if (var12.get() == 1):
        txtButterscotch_Cake.configure(state = NORMAL)
        txtButterscotch_Cake.focus()
        txtButterscotch_Cake.delete('0', END)
        E_Butterscotch_Cake.set("")
    elif(var12.get() == 0):
        txtButterscotch_Cake.configure(state = DISABLED)
        E_Butterscotch_Cake.set("0")
def chkBlack_Forest_Cake():
    if (var13.get() == 1):
        txtBlack_Forest_Cake.configure(state = NORMAL)
        txtBlack_Forest_Cake.focus()
        txtBlack_Forest_Cake.delete('0', END)
        E_Black_Forest_Cake.set("")
    elif(var13.get() == 0):
        txtBlack_Forest_Cake.configure(state = DISABLED)
        E_Black_Forest_Cake.set("0")        
def chkRed_Velvet_Cake():
    if (var14.get() == 1):
        txtRed_Velvet_Cake.configure(state = NORMAL)
        txtRed_Velvet_Cake.focus()
        txtRed_Velvet_Cake.delete('0', END)
        E_Red_Velvet_Cake.set("")
    elif(var14.get() == 0):
        txtRed_Velvet_Cake.configure(state = DISABLED)
        E_Red_Velvet_Cake.set("0")
def chkCaramel_Cake():
    if (var15.get() == 1):
        txtCaramel_Cake.configure(state = NORMAL)
        txtCaramel_Cake.focus()
        txtCaramel_Cake.delete('0', END)
        E_Caramel_Cake.set("")
    elif(var15.get() == 0):
        txtCaramel_Cake.configure(state = DISABLED)
        E_Caramel_Cake.set("0")
def chkCarrot_Cake():
    if (var16.get() == 1):
        txtCarrot_Cake.configure(state = NORMAL)
        txtCarrot_Cake.focus()
        txtCarrot_Cake.delete('0', END)
        E_Carrot_Cake.set("")
    elif(var16.get() == 0):
        txtCarrot_Cake.configure(state = DISABLED)
        E_Carrot_Cake.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10903, 609235)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END,'Receipt Ref:\t\t\t' + Receipt_Ref.get()+'\t'+DateofOrder.get()+"\n")
    txtReceipt.insert(END,'Items\t\t\t\t' + "Cost of Items\n")
    txtReceipt.insert(END,'Tea:\t\t\t\t\t' + E_Tea.get()+"\n")
    txtReceipt.insert(END,'Coffee:\t\t\t\t\t' + E_Coffee.get()+"\n")
    txtReceipt.insert(END,'Lassi:\t\t\t\t\t' + E_Lassi.get()+"\n")
    txtReceipt.insert(END,'Pepsi:\t\t\t\t\t' + E_Pepsi.get()+"\n")
    txtReceipt.insert(END,'Coca Cola:\t\t\t\t\t' + E_Coca_Cola.get()+"\n")
    txtReceipt.insert(END,'Masala Soda:\t\t\t\t\t' + E_Masala_Soda.get()+"\n")
    txtReceipt.insert(END,'Milkshake:\t\t\t\t\t' + E_Milkshake.get()+"\n")
    txtReceipt.insert(END,'Virgin Mojito:\t\t\t\t\t' + E_Virgin_Mojito.get()+"\n")
    txtReceipt.insert(END,'Chocolate Cake:\t\t\t\t\t' + E_Chocolate_Cake.get()+"\n")
    txtReceipt.insert(END,'Vanilla Cake:\t\t\t\t\t' + E_Vanilla_Cake.get()+"\n")
    txtReceipt.insert(END,'Strawberry Cake:\t\t\t\t\t' + E_Strawberry_Cake.get()+"\n")
    txtReceipt.insert(END,'Butterscotch Cake:\t\t\t\t\t' + E_Butterscotch_Cake.get()+"\n")
    txtReceipt.insert(END,'Black Forest Cake:\t\t\t\t\t' + E_Black_Forest_Cake.get()+"\n")
    txtReceipt.insert(END,'Red Velvet Cake:\t\t\t\t\t' + E_Red_Velvet_Cake.get()+"\n")
    txtReceipt.insert(END,'Caramel Cake:\t\t\t\t\t' + E_Caramel_Cake.get()+"\n")
    txtReceipt.insert(END,'Carrot Cake:\t\t\t\t\t' + E_Carrot_Cake.get()+"\n")
    txtReceipt.insert(END,'Cost of Drinks:\t\t\t\t' + CostofDrinks.get()+ '\nTax Paid:\t\t\t\t' + PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Cakes:\t\t\t\t'+ CostofCakes.get()+ '\nSubTotal:\t\t\t\t' + SubTotal.get()+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t' + TotalCost.get()+"\n")
#=========================================================Drinks===================================================================
Tea =Checkbutton(Drinks_F, text="Tea", variable=var1, onvalue=1, offvalue=0, font=('arial',18, 'bold'),
                    bg='Powder Blue', command = chkTea).grid(row=0,sticky=W)
Coffee = Checkbutton(Drinks_F, text="Coffee", variable=var2, onvalue=1, offvalue=0, font=('arial',18, 'bold'),
                   bg='Powder Blue', command = chkCoffee).grid(row=1,sticky=W)
Lassi = Checkbutton(Drinks_F, text="Lassi", variable=var3, onvalue=1, offvalue=0, font=('arial',18, 'bold'),
                    bg='Powder Blue', command = chkLassi ).grid(row=2,sticky=W)
Pepsi = Checkbutton(Drinks_F, text="Pepsi", variable=var4, onvalue=1, offvalue=0, font=('arial',18, 'bold'),
                    bg='Powder Blue', command = chkPepsi).grid(row=3,sticky=W)
Coca_Cola = Checkbutton(Drinks_F, text="Coca Cola", variable=var5, onvalue=1, offvalue=0, font=('arial',18, 'bold'),
                    bg='Powder Blue', command = chkCoca_Cola).grid(row=4,sticky=W)
Masala_Soda = Checkbutton(Drinks_F, text="Masala Soda", variable=var6, onvalue=1, offvalue=0, font=('arial',18, 'bold'),
                    bg='Powder Blue', command = chkMasala_Soda).grid(row=5,sticky=W)
Milkshake = Checkbutton(Drinks_F, text="Milkshake", variable=var7, onvalue=1, offvalue=0, font=('arial',18, 'bold'),
                    bg='Powder Blue', command = chkMilkshake).grid(row=6,sticky=W)
Virgin_Mojito = Checkbutton(Drinks_F, text="Virgin Mojito", variable=var8, onvalue=1, offvalue=0, font=('arial',18, 'bold'),
                    bg='Powder Blue', command = chkVirgin_Mojito).grid(row=7,sticky=W)
#=================================================Entry Box for Drinks==============================================================
txtTea = Entry(Drinks_F, font=('arial',16,'bold'), textvariable=E_Tea,bd=8, width=6, justify=LEFT,state=DISABLED)
txtTea.grid(row=0,column=1)

txtCoffee= Entry(Drinks_F, font=('arial',16,'bold'),textvariable=E_Coffee,bd=8, width=6, justify=LEFT,state=DISABLED)
txtCoffee.grid(row=1,column=1)

txtLassi = Entry(Drinks_F, font=('arial',16,'bold'),textvariable=E_Lassi,bd=8, width=6, justify=LEFT,state=DISABLED)
txtLassi.grid(row=2,column=1)

txtPepsi = Entry(Drinks_F, font=('arial',16,'bold'),textvariable=E_Pepsi,bd=8, width=6, justify=LEFT,state=DISABLED)
txtPepsi.grid(row=3,column=1)

txtCoca_Cola = Entry(Drinks_F, font=('arial',16,'bold'),textvariable=E_Coca_Cola,bd=8, width=6, justify=LEFT,state=DISABLED)
txtCoca_Cola.grid(row=4,column=1)

txtMasala_Soda = Entry(Drinks_F, font=('arial',16,'bold'),textvariable=E_Masala_Soda,bd=8, width=6, justify=LEFT,state=DISABLED)
txtMasala_Soda.grid(row=5,column=1)

txtMilkshake= Entry(Drinks_F, font=('arial',16,'bold'),textvariable=E_Milkshake,bd=8, width=6, justify=LEFT,state=DISABLED)
txtMilkshake.grid(row=6,column=1)

txtVirgin_Mojito = Entry(Drinks_F, font=('arial',16,'bold'),textvariable=E_Virgin_Mojito,bd=8, width=6, justify=LEFT,state=DISABLED)
txtVirgin_Mojito.grid(row=7,column=1)
#==========================================================Cakes=====================================================================
Chocolate_Cake = Checkbutton(Cake_F, text="Chocolate Cake\t\t\t " , variable=var9, onvalue=1, offvalue=0, font=('arial',16, 'bold'),
                    bg="Powder Blue", command=chkChocolate_Cake).grid(row=0,sticky=W)
Vanilla_Cake = Checkbutton(Cake_F, text="Vanilla Cake", variable=var10, onvalue=1, offvalue=0, font=('arial',16, 'bold'),
                    bg="Powder Blue",command=chkVanilla_Cake).grid(row=1,sticky=W)
Strawberry_Cake = Checkbutton(Cake_F, text="Strawberry Cake", variable=var11, onvalue=1, offvalue=0, font=('arial',16, 'bold'),
                    bg="Powder Blue",command=chkStrawberry_Cake).grid(row=2,sticky=W)
Butterscotch_Cake = Checkbutton(Cake_F, text="Butterscotch Cake", variable=var12, onvalue=1, offvalue=0, font=('arial',16, 'bold'),
                    bg="Powder Blue",command=chkButterscotch_Cake ).grid(row=3,sticky=W)
Black_Forest_Cake = Checkbutton(Cake_F, text="Black Forest Cake", variable=var13, onvalue=1, offvalue=0, font=('arial',16, 'bold'),
                    bg="Powder Blue",command=chkBlack_Forest_Cake).grid(row=4,sticky=W)
Red_Velvet_Cake = Checkbutton(Cake_F, text="Red Velvet Cake", variable=var14, onvalue=1, offvalue=0, font=('arial',16, 'bold'),
                    bg="Powder Blue",command=chkRed_Velvet_Cake).grid(row=5,sticky=W)
Caramel_Cake = Checkbutton(Cake_F, text="Caramel Cake", variable=var15, onvalue=1, offvalue=0, font=('arial',16, 'bold'),
                    bg="Powder Blue",command=chkCaramel_Cake).grid(row=6,sticky=W)
Carrot_Cake = Checkbutton(Cake_F, text="Carrot Cake", variable=var16, onvalue=1, offvalue=0, font=('arial',16, 'bold'),
                    bg="Powder Blue",command=chkCarrot_Cake).grid(row=7,sticky=W)
#==================================================Entry Box for Cakes===============================================================
txtChocolate_Cake = Entry(Cake_F, font=('arial',16,'bold'),bd=8, width=6, justify='left',
                       state=DISABLED, textvariable=E_Chocolate_Cake)
txtChocolate_Cake.grid(row=0,column=1)

txtVanilla_Cake= Entry(Cake_F, font=('arial',16,'bold'),bd=8, width=6, justify='left',
                        state=DISABLED, textvariable=E_Vanilla_Cake)
txtVanilla_Cake.grid(row=1,column=1)

txtStrawberry_Cake = Entry(Cake_F, font=('arial',16,'bold'),bd=8, width=6, justify='left',
                            state=DISABLED,textvariable=E_Strawberry_Cake)
txtStrawberry_Cake.grid(row=2,column=1)

txtButterscotch_Cake  = Entry(Cake_F, font=('arial',16,'bold'),bd=8, width=6, justify='left',
                              state=DISABLED,textvariable=E_Butterscotch_Cake)
txtButterscotch_Cake.grid(row=3,column=1)

txtBlack_Forest_Cake = Entry(Cake_F, font=('arial',16,'bold'),bd=8, width=6, justify='left',
                                state=DISABLED,textvariable=E_Black_Forest_Cake)
txtBlack_Forest_Cake.grid(row=4,column=1)

txtRed_Velvet_Cake = Entry(Cake_F, font=('arial',16,'bold'),bd=8, width=6, justify='left',
                                  state=DISABLED,textvariable=E_Red_Velvet_Cake)
txtRed_Velvet_Cake.grid(row=5,column=1)

txtCaramel_Cake= Entry(Cake_F, font=('arial',16,'bold'),bd=8, width=6, justify='left',
                            state=DISABLED,textvariable=E_Caramel_Cake)
txtCaramel_Cake.grid(row=6,column=1)

txtCarrot_Cake  = Entry(Cake_F, font=('arial',16,'bold'),bd=8, width=6, justify='left',
                            state=DISABLED,textvariable=E_Carrot_Cake)
txtCarrot_Cake.grid(row=7,column=1)
#===========================================Total Cost================================================================================
lblCostofDrinks = Label(Cost_F,font=('arial',14, 'bold'), text="Cost of Drinks\t", bg="Powder blue", fg="black",)
lblCostofDrinks.grid(row=0,column=0, sticky=W)
txtCostofDrinks = Entry(Cost_F, font=('arial', 14,'bold'), textvariable=CostofDrinks, bd=7,bg="white",
                        insertwidth=2, justify=RIGHT)
txtCostofDrinks.grid(row=0, column=1)

lblCostofCakes = Label(Cost_F,font=('arial',14, 'bold'), text="Cost of Cakes " ,bg="Powder blue", fg="black",)
lblCostofCakes .grid(row=1,column=0, sticky=W)
txtCostofCakes = Entry(Cost_F,font=('arial', 14,'bold'), textvariable=CostofCakes, bd=7,bg="white",
                        insertwidth=2, justify=RIGHT)
txtCostofCakes.grid(row=1, column=1)

lblServiceCharge = Label(Cost_F,font=('arial',14, 'bold'), text="Service Charge " ,bg="Powder blue", fg="black",)
lblServiceCharge.grid(row=2,column=0, sticky=W)
txtServiceCharge = Entry(Cost_F,font=('arial', 14,'bold'), textvariable=ServiceCharge, bd=7,bg="white",
                        insertwidth=2, justify=RIGHT)
txtServiceCharge.grid(row=2, column=1)
#============================================Payment Information======================================================================
lblPaidTax = Label(Cost_F,font=('arial',14, 'bold'), text="\tPaid Tax" , bd=7,  bg="Powder blue", fg="black",)
lblPaidTax.grid(row=0,column=2, sticky=W)
txtPaidTax  = Entry(Cost_F,font=('arial', 14,'bold'), textvariable=PaidTax, bd=7,bg="white",
                        insertwidth=2, justify=RIGHT)
txtPaidTax.grid(row=0,column=3)

lblSubTotal = Label(Cost_F,font=('arial',14, 'bold'), text="\tSub Total" , bd=7, bg="Powder blue", fg="black",)
lblSubTotal.grid(row=1,column=2, sticky=W)
txtSubTotal   = Entry(Cost_F,font=('arial', 14,'bold'), textvariable=SubTotal, bd=7,bg="white",
                        insertwidth=2, justify=RIGHT)
txtSubTotal.grid(row=1,column=3)

lblTotalCost = Label(Cost_F,font=('arial',14, 'bold'), text="\tTotal Cost", bd=7, bg="Powder blue", fg="black",)
lblTotalCost.grid(row=2,column=2, sticky=W)
txtTotalCost = Entry(Cost_F,font=('arial', 14,'bold'), textvariable=TotalCost, bd=7,bg="white",insertwidth=2,
                       justify=RIGHT)           
txtTotalCost.grid(row=2,column=3)
#=============================================================Receipt=================================================================
txtReceipt = Text(Receipt_F, width=46, height=12, bg="white", bd=4, font=('arial', 12,'bold'))
txtReceipt.grid(row=0, column=0)
#=========================================================== Buttons==================================================================
btnTotal = Button(Buttons_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="Total"
                  ,bg="Powder blue", command=CostofItem).grid(row=0, column=0)
btnReceipt = Button(Buttons_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="Receipt"
                  ,bg="Powder blue", command=Receipt).grid(row=0, column=1)
btnReset = Button(Buttons_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="Reset"
                  ,bg="Powder blue", command= Reset).grid(row=0, column=2)
btnExit = Button(Buttons_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="Exit"
                  ,bg="Powder blue", command = iExit).grid(row=0,column=3)
#===========================================================Calculator Display========================================================
def btnClick(numbers):
  global operator
  operator = operator + str(numbers)
  text_Input.set(operator)

def btnClear():
  global operator
  operator = ""
  text_Input.set("")

def btnEquals():
  global operator
  sumup = str(eval(operator))
  text_Input.set(sumup)
  operator = ""

  
txtDisplay = Entry(Cal_F, width=45, bg="white", bd=4, font=('arial', 12,'bold'), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0, column=0,columnspan=4, pady=1)
txtDisplay.insert(0, "0")
#===========================================================Calculator Buttons========================================================
btn7 =Button(Cal_F, padx=16, pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="7"
                  ,bg="Powder blue",command=lambda:btnClick(7)).grid(row=2, column=0)
btn8 = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="8"
                  ,bg="Powder blue",command=lambda:btnClick(8)).grid(row=2, column=1)
btn9 = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="9"
                  ,bg="Powder blue",command=lambda:btnClick(9)).grid(row=2, column=2)
btnAdd = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="+"
                  ,bg="Powder blue",command=lambda:btnClick("+")).grid(row=2, column=3)
#===========================================================Calculator Buttons========================================================
btn4 = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="4"
                  ,command=lambda:btnClick(4)).grid(row=3, column=0)
btn5 = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="5"
                  ,command=lambda:btnClick(5)).grid(row=3, column=1)
btn6 = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="6"
                  ,command=lambda:btnClick(6)).grid(row=3, column=2)
btnSub = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="-"
                  ,bg="Powder blue",command=lambda:btnClick("-")).grid(row=3, column=3)
#===========================================================Calculator Buttons========================================================
btn1 = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="1"
                  ,command=lambda:btnClick(1)).grid(row=4, column=0)
btn2 = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="2"
                  ,command=lambda:btnClick(2)).grid(row=4, column=1)
btn3 = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="3"
                  ,command=lambda:btnClick(3)).grid(row=4, column=2)
btnMulti = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="*"
                  ,bg="Powder blue",command=lambda:btnClick("*")).grid(row=4, column=3)
#===========================================================Calculator Buttons========================================================
btn0 = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="0"
                  ,bg="Powder blue",command=lambda:btnClick(0)).grid(row=5, column=0)
btnClear = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="C"
                  ,bg="Powder blue",command=btnClear).grid(row=5, column=1)
btnEquals = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="="
                  ,bg="Powder blue",command=btnEquals).grid(row=5, column=2)
btnDiv = Button(Cal_F, padx=16,pady=1, bd=7, fg="black",font=('arial', 16,'bold'), width=4, text="/"
                  ,bg="Powder blue",command=lambda:btnClick("/")).grid(row=5, column=3)

root.mainloop()
