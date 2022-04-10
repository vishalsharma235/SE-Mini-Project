from tkinter import *
import mysql.connector
import random
from tkinter import messagebox
import tkinter.font as all_font
import math

db=mysql.connector.connect(host="localhost", user="root", passwd="",database="pharmacy")
c=db.cursor(buffered=True)

t = Tk()
v=StringVar()
v.set('m')
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v1.set(0)
v2.set(2)
v3.set(1)
type=-1
user="/0"
custid=0
hopid=0
presc=0
medlist=[]
medtype="/0"
medtype1="/0"
medtype2="/0"
medtype3="/0"
detail1="/0"
detail2="/0"
detail3="/0"
detail4="/0"

t.title("Pharmacy Management System 24x7")
t.iconbitmap(r'pharmacyicon.ico')
t.resizable(width=FALSE, height=FALSE)

t.geometry("1200x600+180+110")
cust_image = PhotoImage(file='team.png')
hos_image = PhotoImage(file='hospital.png')
wallpaperc = PhotoImage(file='1c.png')
wallpaperh = PhotoImage(file='1h.png')
ch=PhotoImage(file="ch.png")
image1=PhotoImage(file="Boxbgf.png")
image2=PhotoImage(file="Boxbg1.png")
image=PhotoImage(file="a1.png")
imagepg1=PhotoImage(file="a1copy.png")
imagepg2=PhotoImage(file="a1h.png")
imagepg3=PhotoImage(file="a1c.png")
imagepg4=PhotoImage(file="a2hosp.png")
imagepg5=PhotoImage(file="a2cust.png")
inventory=PhotoImage(file="stock.png")
rupee1=PhotoImage(file="rupee1.png")
rupee2=PhotoImage(file="rupee2.png")
prescimg = PhotoImage(file="prescription.png")

a=all_font
b=all_font

font = all_font.Font(weight='bold',size=45,family="Nueva Std Cond")

b1 = all_font.Font(weight="bold",size=16,family="Tw Cen MT")
a = all_font.Font(weight="bold",size=20,family="Tw Cen MT")
a2 = all_font.Font(weight="bold",size=16,family="Tw Cen MT")
a1 = all_font.Font(weight="bold",size=24,family="Tw Cen MT")
b = all_font.Font(weight="bold",size=16,family="Tw Cen MT")
pfont = all_font.Font(weight="bold",size=11,family="Tw Cen MT")

#-------------------------------------------------------------

def cartfunc():
    cartpage = Toplevel(t)
    cartpage.title("  Your Cart  ")
    cartpage.minsize(400, 650)
    cartpage.iconbitmap(r'pharmacyicon.ico')
    cartpage.geometry('400x650+1100+10')
    Label(cartpage, image=ch).place(relwidth=1, relheight=1)


    def proceed():
        page2 = Toplevel()
        t.withdraw()

        page2.geometry('400x650')
        Label(page2, image=ch).place(relwidth=1, relheight=1)

        Label(page2, image=image1,).place(relwidth=1, relheight=1)
        Label(page2, text='Payment Successful').place(x=150, y=550)
        ex = Button(page2, text="  Exit  ", bd=5, command=page2.destroy).place(x=150, y=600)

    def payment_option():
        page1 = Toplevel()
        t.withdraw()
        page1.geometry('400x650')
        Label(page1, image=ch).place(relwidth=1, relheight=1)

        Radiobutton(page1, text="Cash on Delivery", font=('Calibri', 16), variable=v, value=1).place(x=10, y=60)
        Radiobutton(page1, text="Credit/Debit Card, Net Banking,UPI,Wallet", font=('Calibri', 16), variable=v,
                    value=2).place(x=10, y=90)
        Radiobutton(page1, text="Credit/Debit Card", font=('Calibri', 16), variable=v, value=3).place(x=10, y=120)
        Radiobutton(page1, text="Net Banking", font=('Calibri', 16), variable=v, value=4).place(x=10, y=150)
        Radiobutton(page1, text="PayU(Wallet,UPI,GooglePay)", font=('Calibri', 16), variable=v, value=5).place(x=10,
                                                                                                                  y=180)
        B = Button(page1, text="  Proceed to Pay ", bd=5, command=lambda: [proceed(), page1.destroy()]).place(x=150, y=600)

    c.execute("SELECT * FROM temp_cart;")
    i = 0
    e = Label(cartpage, text='Name', width=25, bg='grey', fg='black')
    e.grid(row=0, column=0)
    e = Label(cartpage, text='Price', width=10, bg='grey', fg='black')
    e.grid(row=0, column=1)
    e = Label(cartpage, text='Quantity', width=10, bg='grey', fg='black')
    e.grid(row=0, column=2)
    e = Label(cartpage, text='Sub-Total', width=10, bg='grey', fg='black')
    e.grid(row=0, column=3)
    for student in c:
        for j in range(len(student)):
            if j == 0:
                e = Label(cartpage, text=student[j], width=25, fg='black')
                e.grid(row=i + 1, column=j)
            else:
                e = Label(cartpage, text=student[j], width=10, fg='black')
                e.grid(row=i + 1, column=j)
        i = i + 1
    c.execute("SELECT sum(Sub_Total) FROM temp_cart")
    total = c.fetchone()
    e = Label(cartpage, text=total, width=10, bg='yellow', fg='black')
    e.grid(row=i+2, column=3)

    B = Button(cartpage, text="  Proceed  ", bd=5, command=lambda: [payment_option(), cartpage.destroy()]).place(x=150, y=600)

def cart():
    global presc
    global medlist
    cartfunc()


def customerinfo():
    global type
    global username
    custinfo=Toplevel(t)
    custinfo.title("Profile")
    custinfo.iconbitmap(r'pharmacyicon.ico')
    custinfo.resizable(width=FALSE, height=FALSE)
    custinfo.geometry('400x650+10+10')

    def disable_event():
        pass

    if(type == 0):
        Label(custinfo, image=wallpaperc).place(relwidth=1, relheight=1)
        sql1="SELECT * FROM customer where Customer_id=%s"
        global custid
        x=(custid,)
        c.execute(sql1,x)
        result=c.fetchall()
        list(result)
        username=result[0][1]
        a=120
        for i in range(len(result[0])):
            x = result[0][i]
            if i==3:
                Label(custinfo, text=x, font=("Segoe Script", 10, "bold"), bg="#636363", fg="#FFFFFF").place(x=165, y=a)
            else:
                Label(custinfo, text=x, font=("Segoe Script", 11, "bold"), bg="#636363", fg="#FFFFFF").place(x=210, y=a)
            a += 88

    if(type == 1):
        Label(custinfo, image=wallpaperh).place(relwidth=1, relheight=1)
        sql2 = "SELECT * FROM hospital where Hospital_id=%s"
        global hopid
        x = (hopid,)
        a=110
        c.execute(sql2, x)
        result = c.fetchall()
        list(result)
        username=result[0][2]
        for i in range(len(result[0])):
            x = result[0][i]
            if i==4:
                Label(custinfo, text=str, font=("Segoe Script", 10, "bold"), bg="#6e6e6e", fg="#FFFFFF").place(x=155, y=a)
            if i==1:
                str1=result[0][1]
                str=str1.replace("Hospital","")
                Label(custinfo, text=str, font=("Segoe Script", 10, "bold"), bg="#6e6e6e", fg="#FFFFFF").place(x=202, y=a)
            else :
                Label(custinfo, text=x, font=("Segoe Script",10, "bold"), bg="#6e6e6e", fg="#FFFFFF").place(x=210,y=a)
            a+=75

    def editdetails():
        ed=Toplevel(custinfo)
        custinfo.withdraw()
        ed.title("Edit Profile")
        ed.iconbitmap(r'pharmacyicon.ico')
        ed.resizable(width=FALSE, height=FALSE)
        ed.geometry('400x650+10+10')
        Label(ed, image=ch).place(relwidth=1, relheight=1)
        ed.protocol("WM_DELETE_WINDOW", disable_event)

        def editback():
            ed.withdraw()

        if(type == 0):
            global custid

            def box_cus():
                if(variable.get() == " First Name "):
                    def update_custfn():
                        fn = E1.get()
                        if (variable.get() == " First Name "):
                            val = (fn,custid)
                            sql = "UPDATE customer SET Customer_fn = %s WHERE Customer_id = %s"
                            c.execute(sql,val)
                            db.commit()
                            l=Label(ed,text="UPDATED",font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                            l.place(x=130,y=500)
                            l.after(900,l.place_forget)

                    Label(ed,text=" First Name ",font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35,y=300)
                    E1=Entry(ed,font=("Segoe Script", 12, "bold"),width=18)
                    E1.place(x=155,y=300)
                    Button(ed, text="Update", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 12),relief=GROOVE,command=update_custfn).place(x=155,y=380)
                elif (variable.get() == " Last Name "):
                    def update_custln():
                        ln = E1.get()
                        if (variable.get() == " Last Name "):
                            val = (ln,custid)
                            sql = "UPDATE customer SET Customer_ln = %s WHERE Customer_id = %s"
                            c.execute(sql,val)
                            db.commit()
                            l=Label(ed,text="UPDATED",font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                            l.place(x=130,y=500)
                            l.after(900,l.place_forget)

                    Label(ed, text=" Last Name ", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35, y=300)
                    E1=Entry(ed, font=("Segoe Script", 12, "bold"), width=18)
                    E1.place(x=155,y=300)
                    Button(ed, text="Update", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 12),
                           relief=GROOVE,command=update_custln).place(x=155, y=380)
                elif (variable.get() == "  Email Id  "):
                    def update_custemail():
                        email = E1.get()
                        if (variable.get() == "  Email Id  "):
                            if(('@' not in (email)) or ((email).endswith('.com') == False) or (email.count('@') != 1)):
                                messagebox.showwarning("Error","Email should have only one (@) and should end with (.com)")
                            else:
                                val = (email,custid)
                                sql = "UPDATE customer SET Email_id = %s WHERE Customer_id = %s"
                                c.execute(sql,val)
                                db.commit()
                                l=Label(ed,text="UPDATED",font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                                l.place(x=130,y=500)
                                l.after(900,l.place_forget)


                    Label(ed, text="  Email Id  ", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35, y=300)
                    E1=Entry(ed, font=("Segoe Script", 12, "bold"), width=18)
                    E1.place(x=155,y=300)
                    Button(ed, text="Update", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 12),
                           relief=GROOVE,command=update_custemail).place(x=155, y=380)
                elif (variable.get() == "Contact No. "):
                    def update_custcon():
                        contact = E1.get()
                        if (variable.get() == "Contact No. "):
                            if(contact == "" or len(contact) > 10 or len(contact) < 10):
                                messagebox.showwarning("Error","Contact number should be of 10 digits")
                            else:
                                val = (contact,custid)
                                sql = "UPDATE customer SET Contact_no = %s WHERE Customer_id = %s"
                                c.execute(sql,val)
                                db.commit()
                                l=Label(ed,text="UPDATED",font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                                l.place(x=130,y=500)
                                l.after(900,l.place_forget)

                    Label(ed, text="Contact No. ", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35, y=300)
                    E1=Entry(ed, font=("Segoe Script", 12, "bold"), width=18)
                    E1.place(x=155,y=300)
                    Button(ed, text="Update", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 12),
                           relief=GROOVE,command=update_custcon).place(x=155, y=380)
                elif (variable.get() == "   Gender   "):
                    def update_custgender():
                        if (variable1.get() == "                  Male                 "):
                            g= "m"
                            val = (g, custid)
                            sql = "UPDATE customer SET Gender = %s WHERE Customer_id = %s"
                            c.execute(sql, val)
                            db.commit()
                            l = Label(ed, text="UPDATED", font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                            l.place(x=130, y=500)
                            l.after(900, l.place_forget)
                        elif(variable1.get() == "                 Female                "):
                            g = "f"
                            val = (g,custid)
                            sql = "UPDATE customer SET Gender = %s WHERE Customer_id = %s"
                            c.execute(sql,val)
                            db.commit()
                            l=Label(ed,text="UPDATED",font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                            l.place(x=130,y=500)
                            l.after(900,l.place_forget)
                    Label(ed, text="   Gender   ", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35, y=300)
                    G=OptionMenu(ed,variable1,"                  Male                 ", "                 Female                ")
                    G.place(x=155,y=300,)
                    G.config(font=(9))
                    Button(ed, text="Update", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 12),
                           relief=GROOVE,command=update_custgender).place(x=155, y=380)

            sql1 = "SELECT * FROM customer where Customer_id=%s"
            global custid
            x = (custid,)
            c.execute(sql1, x)
            Label(ed, text="Customer ID:", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=95, y=120)
            Label(ed, text=x, font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=250, y=120)
            Label(ed, text="EDIT:", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35, y=200)
            variable=StringVar(ed)
            variable1=StringVar(ed)
            variable1.set("                Gender               ")
            d=OptionMenu(ed,variable," First Name "," Last Name ","  Email Id  ","Contact No. ","   Gender   ")
            d.place(x=110,y=200)
            d.config(font=(9))
            Button(ed, text="Next", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 10), relief=GROOVE,command=box_cus).place(x=300,y=200)


        if (type == 1):
            global hopid

            def box_hos():
                if(variable.get() == "Hospital Name"):
                    def update_hosn():
                        hn = E1.get()
                        if (variable.get() == "Hospital Name"):
                            val = (hn,hopid)
                            sql = "UPDATE hospital SET Hospital_name = %s WHERE Hospital_id = %s"
                            c.execute(sql,val)
                            db.commit()
                            l=Label(ed,text="UPDATED",font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                            l.place(x=130,y=500)
                            l.after(900,l.place_forget)

                    Label(ed,text="Hospital Name",font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35,y=300)
                    E1=Entry(ed,font=("Segoe Script", 12, "bold"),width=15)
                    E1.place(x=185,y=300)
                    Button(ed, text="Update", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 12),
                           relief=GROOVE,command=update_hosn).place(x=185, y=380)
                elif (variable.get() == "Repres. Name"):
                    def update_hosrn():
                        rn = E1.get()
                        if (variable.get() == "Repres. Name"):
                            val = (rn,hopid)
                            sql = "UPDATE hospital SET R_name = %s WHERE Hospital_id = %s"
                            c.execute(sql,val)
                            db.commit()
                            l=Label(ed,text="UPDATED",font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                            l.place(x=130,y=500)
                            l.after(900,l.place_forget)


                    Label(ed, text="  Repre. Name ", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35, y=300)
                    E1=Entry(ed, font=("Segoe Script", 12, "bold"), width=15)
                    E1.place(x=185,y=300)
                    Button(ed, text="Update", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 12),
                           relief=GROOVE,command=update_hosrn).place(x=185, y=380)
                elif (variable.get() == "Repres. Id"):
                    def update_hosrid():
                        rid = E1.get()
                        if (variable.get() == "Repres. Id"):
                            if (len(rid) > 5 or len(rid) < 5 or rid == ""):
                                messagebox.showwarning("Error",
                                                       "Representative Id should be of 5 digits")
                            else:
                                val = (rid, hopid)
                                sql = "UPDATE hospital SET R_id = %s WHERE Hospital_id = %s"
                                c.execute(sql, val)
                                db.commit()
                                l = Label(ed, text="UPDATED", font=("Segoe Script", 15, "bold"), bg="#636363",
                                          fg="#FFFFFF")
                                l.place(x=130, y=500)
                                l.after(900, l.place_forget)

                    Label(ed, text="    Repre. Id  ", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35, y=300)
                    E1=Entry(ed, font=("Segoe Script", 12, "bold"), width=15)
                    E1.place(x=185,y=300)
                    Button(ed, text="Update", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 12),
                           relief=GROOVE,command=update_hosrid).place(x=185, y=380)

                elif (variable.get() == "Email Id"):
                    def update_hosemail():
                        email1 = E1.get()
                        if (variable.get() == "Email Id"):
                            if(('@' not in (email1)) or ((email1).endswith('.com') == False) or (email1.count('@') != 1)):
                                messagebox.showwarning("Error","Email should have only one (@) and should end with (.com)")
                            else:
                                val = (email1,hopid)
                                sql = "UPDATE hospital SET Email_id = %s WHERE Hospital_id = %s"
                                c.execute(sql,val)
                                db.commit()
                                l=Label(ed,text="UPDATED",font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                                l.place(x=130,y=500)
                                l.after(900,l.place_forget)

                    Label(ed, text="   Email Id   ", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35, y=300)
                    E1=Entry(ed, font=("Segoe Script", 12, "bold"), width=15)
                    E1.place(x=185,y=300)
                    Button(ed, text="Update", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 12),
                           relief=GROOVE,command=update_hosemail).place(x=185, y=380)



                elif (variable.get() == "Contact No"):
                    def update_hoscon():
                        contact = E1.get()
                        if (variable.get() == "Contact No"):
                            if(contact == "" or len(contact) > 10 or len(contact) < 10):
                                messagebox.showwarning("Error","Contact number should be of 10 digits")
                            else:
                                val = (contact,hopid)
                                sql = "UPDATE hospital SET Contact_no = %s WHERE Hospital_id = %s"
                                c.execute(sql,val)
                                db.commit()
                                l=Label(ed,text="UPDATED",font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                                l.place(x=130,y=500)
                                l.after(900,l.place_forget)

                    Label(ed, text="   Contact No  ", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35, y=300)
                    E1=Entry(ed, font=("Segoe Script", 12, "bold"), width=15)
                    E1.place(x=185,y=300)
                    Button(ed, text="Update", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 12),
                           relief=GROOVE,command=update_hoscon).place(x=185, y=380)

                elif (variable.get() == "Gender"):
                    def update_hosgender():
                        if (variable1.get() == "             Male             "):
                            g1 = "m"
                            val = (g1, hopid)
                            sql = "UPDATE hospital SET Gender = %s WHERE Hospital_id = %s"
                            c.execute(sql, val)
                            db.commit()
                            l = Label(ed, text="UPDATED", font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                            l.place(x=130, y=500)
                            l.after(900, l.place_forget)
                        elif(variable1.get() == "            Female            "):
                            g1 = "f"
                            val = (g1,hopid)
                            sql = "UPDATE hospital SET Gender = %s WHERE Hospital_id = %s"
                            c.execute(sql,val)
                            db.commit()
                            l=Label(ed,text="UPDATED",font=("Segoe Script", 15, "bold"),bg="#636363", fg="#FFFFFF")
                            l.place(x=130,y=500)
                            l.after(900,l.place_forget)

                    Label(ed, text="       Gender    ", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35, y=300)
                    G = OptionMenu(ed, variable1, "             Male             ", "            Female            ")
                    G.place(x=185, y=300)
                    G.config(font=(9))
                    Button(ed, text="Update", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 12),
                           relief=GROOVE,command=update_hosgender).place(x=185, y=380)

            sql2 = "SELECT * FROM hospital where Hospital_id=%s"
            global hopid
            x = (hopid,)
            c.execute(sql2, x)
            Label(ed, text="Customer ID:", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=95,y=120)
            Label(ed, text=x, font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=250, y=120)
            Label(ed, text="EDIT:", font=("Segoe Script", 12, "bold"), bg="#636363", fg="#FFFFFF").place(x=35, y=200)
            variable = StringVar(ed)
            variable1 = StringVar(ed)
            variable1.set("           Gender           ")
            d = OptionMenu(ed, variable, "Hospital Name", "Repres. Name","Repres. Id", "Contact No","Email Id", "Gender")
            d.place(x=110, y=200)
            d.config(font=(9))
            Button(ed,text="Next",bg="#636363",fg="#FFFFFF",font=("Segoe Script",10),relief=GROOVE,command=box_hos).place(x=300,y=200)


        Button(ed,text="BACK", bg="#636363",fg="#FFFFFF",font=("Segoe Script",9),relief=GROOVE,command=editback).place(x=1, y=1)

    def back():
        custinfo.withdraw()
    custinfo.protocol("WM_DELETE_WINDOW", disable_event)
    Button(custinfo, text="EDIT", bg="#636363",fg="#FFFFFF",font=("Segoe Script",9),relief=GROOVE,command=editdetails).place(x=355,y=0)
    Button(custinfo, text="BACK", bg="#636363", fg="#FFFFFF", font=("Segoe Script", 9), relief=GROOVE,command=back).place(x=1, y=0)

def username():
    global user
    if(type==0):
        sql1 = "SELECT Customer_fn FROM customer where Customer_id=%s"
        global custid
        x = (custid,)
        c.execute(sql1, x)
        result = c.fetchone()
        list(result)
        user = result[0]
    if(type==1):
        sql2 = "SELECT R_name FROM hospital where Hospital_id=%s"
        global hopid
        x = (hopid,)
        c.execute(sql2, x)
        result = c.fetchone()
        list(result)
        user = result[0]

def logout():
    exit=messagebox.askquestion("Logging Out", "Are you sure?")
    if exit == 'yes':
        c.execute('TRUNCATE TABLE temp_cart')
        t.destroy()

def stockinfo():
    stock = Toplevel()
    stock.title("Inventory")
    stock.iconbitmap(r'pharmacyicon.ico')
    stock.geometry('460x747+10+0')
    stock.resizable(width=FALSE, height=FALSE)
    inventory = PhotoImage(file="stock.png")
    Label(stock, image=inventory).place(relwidth=1, relheight=1)

    f1 = all_font.Font(size=9, family="Segeo Script")

    def stockm():
        Label(stock, image=inventory).place(relwidth=1, relheight=1)
        x = ("M%",)
        sql = "SELECT ID,M_name,Available,Exp_Date from inventory natural join medicine where (Medicine_id=ID) and Medicine_id like %s";
        c.execute(sql, x)
        result = c.fetchall()
        list(result)
        a = 70
        for i in range(len(result)):
            date = str(result[i][3])
            Label(stock, text=result[i][0]).place(x=23, y=a)
            Label(stock, text=result[i][1], font=f1).place(x=83, y=a + 2)
            Label(stock, text=result[i][2]).place(x=303, y=a)
            Label(stock, text=date).place(x=350, y=a)
            a += 23

        buttons()

    def stockhh():
        Label(stock, image=inventory).place(relwidth=1, relheight=1)
        x = ("HH%",)
        sql = "SELECT ID,CP_name,Available,Exp_Date from inventory natural join care_products where (C_id=ID) and C_id like %s;";
        c.execute(sql, x)
        result = c.fetchall()
        list(result)
        a = 70
        for i in range(len(result)):
            date = str(result[i][3])
            Label(stock, text=result[i][0]).place(x=23, y=a)
            Label(stock, text=result[i][1], font=f1).place(x=83, y=a + 2)
            Label(stock, text=result[i][2]).place(x=303, y=a)
            Label(stock, text=date).place(x=350, y=a)
            a += 23

        buttons()

    def stockhp():
        Label(stock, image=inventory).place(relwidth=1, relheight=1)
        x = ("HP%",)
        sql = "SELECT ID,M_name,Available,Exp_Date from inventory natural join medicine where (Medicine_id=ID) and Medicine_id like %s";
        c.execute(sql, x)
        result = c.fetchall()
        list(result)
        a = 70
        for i in range(len(result)):
            date = str(result[i][3])
            Label(stock, text=result[i][0]).place(x=23, y=a)
            Label(stock, text=result[i][1], font=f1).place(x=83, y=a + 2)
            Label(stock, text=result[i][2]).place(x=303, y=a)
            Label(stock, text=date).place(x=350, y=a)
            a += 23

        buttons()

    def stockpm():
        Label(stock, image=inventory).place(relwidth=1, relheight=1)
        x = ("PM%",)
        sql = "SELECT ID,M_name,Available,Exp_Date from inventory natural join medicine where (Medicine_id=ID) and Medicine_id like %s";
        c.execute(sql, x)
        result = c.fetchall()
        list(result)
        a = 70
        for i in range(len(result)):
            date = str(result[i][3])
            Label(stock, text=result[i][0]).place(x=23, y=a)
            Label(stock, text=result[i][1], font=f1).place(x=83, y=a + 2)
            Label(stock, text=result[i][2]).place(x=303, y=a)
            Label(stock, text=date).place(x=350, y=a)
            a += 23

        buttons()

    def stocksc():
        Label(stock, image=inventory).place(relwidth=1, relheight=1)
        x = ("SC%",)
        sql = "SELECT ID,CP_name,Available,Exp_Date from inventory natural join care_products where (C_id=ID) and C_id like %s;";
        c.execute(sql, x)
        result = c.fetchall()
        list(result)
        a = 70
        for i in range(len(result)):
            date = str(result[i][3])
            Label(stock, text=result[i][0]).place(x=23, y=a)
            Label(stock, text=result[i][1], font=f1).place(x=83, y=a + 2)
            Label(stock, text=result[i][2]).place(x=303, y=a)
            Label(stock, text=date).place(x=350, y=a)
            a += 23

        buttons()

    def stocka():
        Label(stock, image=inventory).place(relwidth=1, relheight=1)
        x = ("A%",)
        sql = "SELECT ID,AM_name,Available,Exp_Date from inventory natural join ayurvedic_med where (AM_id=ID);"
        c.execute(sql)
        result = c.fetchall()
        list(result)
        a = 70
        for i in range(len(result)):
            date = str(result[i][3])
            Label(stock, text=result[i][0]).place(x=23, y=a)
            Label(stock, text=result[i][1], font=f1).place(x=83, y=a + 2)
            Label(stock, text=result[i][2]).place(x=303, y=a)
            Label(stock, text=date).place(x=350, y=a)
            a += 23

        buttons()

    def stockse():
        Label(stock, image=inventory).place(relwidth=1, relheight=1)
        sql = "SELECT ID,S_name,Available,Exp_Date from inventory natural join surgical_products where (SP_id=ID);"
        c.execute(sql)
        result = c.fetchall()
        list(result)
        a = 70
        for i in range(len(result)):
            date = str(result[i][3])
            Label(stock, text=result[i][0]).place(x=23, y=a)
            Label(stock, text=result[i][1], font=f1).place(x=83, y=a + 2)
            Label(stock, text=result[i][2]).place(x=303, y=a)
            Label(stock, text=date).place(x=350, y=a)
            a += 23

        buttons()

    def stockg():
        Label(stock, image=inventory).place(relwidth=1, relheight=1)
        sql = "SELECT ID,GItem_name,Available,Exp_Date from inventory natural join general_items where (GItem_id=ID);"
        c.execute(sql)
        result = c.fetchall()
        list(result)
        a = 70
        for i in range(len(result)):
            date = str(result[i][3])
            Label(stock, text=result[i][0]).place(x=23, y=a)
            Label(stock, text=result[i][1], font=f1).place(x=83, y=a + 2)
            Label(stock, text=result[i][2]).place(x=303, y=a)
            Label(stock, text=date).place(x=350, y=a)
            a += 23

        buttons()

    def buttons():
        Button(stock, text="Medicine", relief=RAISED, bg="white", bd=3, command=stockm).place(x=45, y=650)
        Button(stock, text="Health & Hygiene", relief=RAISED, bg="white", bd=3, command=stockhh).place(x=223, y=650)
        Button(stock, text="Homeopathic", relief=RAISED, bg="white", bd=3, command=stockhp).place(x=123, y=650)
        Button(stock, text="Pet Care", relief=RAISED, bg="white", bd=3, command=stockpm).place(x=347, y=650)
        Button(stock, text="Skin Care", relief=RAISED, bg="white", bd=3, command=stocksc).place(x=45, y=690)
        Button(stock, text="Ayurvedic", relief=RAISED, bg="white", bd=3, command=stocka).place(x=117, y=690)
        Button(stock, text="Surgical Equipments", relief=RAISED, bg="white", bd=3, command=stockse).place(x=192, y=690)
        Button(stock, text="General Items", relief=RAISED, bg="white", bd=3, command=stockg).place(x=322, y=690)

    buttons()


#-------------------------------------------------------------
#mainpage

def mp():

    c2 = ("Arial 8 bold")
    c1 = ("Arial 11 bold")
    c3 = ("Arial 11")
    count=0
    a=0
    counter=1
    spin1 = IntVar()
    spin2 = IntVar()
    spin3 = IntVar()
    spin4 = IntVar()
    spin5 = IntVar()
    spin6 = IntVar()
    spin7 = IntVar()
    spin8 = IntVar()

    # -------------------------------------------------------------
    # topdesign

    t = Toplevel()
    t.title("Pharmacy Management System 24x7")
    t.iconbitmap(r'pharmacyicon.ico')
    t.geometry('755x770+370+10')
    t.resizable(width=FALSE, height=FALSE)
    def disable_event():
        pass
    t.protocol("WM_DELETE_WINDOW", disable_event)
    topbar = Canvas(t, height=62, width=750, bg="grey")
    wallpaper = PhotoImage(file="bg1.png")
    Label(t, image=wallpaper).place(y=63, relwidth=1, relheight=1)
    topbar.create_rectangle(0, 0, 755, 15, fill="#000000")
    topbar.create_rectangle(0, 10, 755, 25, fill="#252525")
    topbar.create_rectangle(0, 20, 755, 35, fill="#4C4C4C")
    topbar.create_rectangle(0, 30, 755, 45, fill="#6D6D6D")
    topbar.create_rectangle(0, 40, 755, 62, fill="#DDDDDD")
    topbar.pack()
    # -------------------------------------------------------------


    global user
    username()
    str="Welcome, "
    str2=str+user
    Label(t,text=str2,fg="black", bg="#DDDDDD").place(x=320,y=41)

    # -------------------------------------------------------------
    #hoverfuctions

    def entere(e):
        hover.place(x=718, y=41)
        hover.configure(text="Exit")
    def leavee(e):
        hover.configure(text="")

    def enterc(e):
        hover.place(x=682, y=41)
        hover.configure(text="Cart")
    def leavec(e):
        hover.configure(text="")

    def entercust(e):
        hover.place(x=0, y=41)
        hover.configure(text="Profile")
    def leavecust(e):
        hover.configure(text="")

    def enterst(e):
        hover.place(x=38, y=41)
        hover.configure(text="Stock")
    def leavest(e):
        hover.configure(text="")

    # -------------------------------------------------------------

    hover = Label(t, text="", relief=FLAT, bg="#DDDDDD")

    cart_image = PhotoImage(file='cart.png')
    cart_button = Button(t, image=cart_image, bg="white", command=cart)
    cart_button.bind("<Enter>", enterc)
    cart_button.bind("<Leave>", leavec)
    cart_button.place(x=682, y=7)

    user_image = PhotoImage(file='user.png')
    user_button = Button(t, image=user_image, bg="white", command=customerinfo)
    user_button.bind("<Enter>", entercust)
    user_button.bind("<Leave>", leavecust)
    user_button.place(x=7, y=7)

    stock_image = PhotoImage(file='inventory.png')
    stock_button = Button(t, image=stock_image, bg="white", command=stockinfo)
    stock_button.bind("<Enter>", enterst)
    stock_button.bind("<Leave>", leavest)
    stock_button.place(x=42, y=7)


    exit_image = PhotoImage(file='logout.png')
    exit_button = Button(t, image=exit_image, bg="white", command=logout)
    exit_button.bind("<Enter>", entere)
    exit_button.bind("<Leave>", leavee)
    exit_button.place(x=717, y=7)

    # -------------------------------------------------------------
    #valuesdisplay

    def canvas():

        def add_to_cart(name, price, qunt):
            total = price * qunt
            query = f"INSERT INTO temp_cart (M_name,Price,Quantity,Sub_Total) VALUES ('{name}', {price}, {qunt}, {total});"
            query1 = "UPDATE inventory SET Available = Available - %d, Sold = Sold + %d " \
                     "WHERE ID IN (" \
                     "SELECT Medicine_id FROM medicine " \
                     "WHERE M_name= '%s')" % (qunt, qunt, name)
            c.execute(query)
            c.execute(query1)
            db.commit()
            i = Label(t, text="✔ Added To Cart", font=c3, bg="black", fg="white")
            i.place(x=325, y=380)
            i.after(1200, i.place_forget)



        def destruct():
            f1.destroy()
            f2.destroy()
            f3.destroy()
            f4.destroy()

        def update_a():
            global a
            a += 4
            destruct()
            canvas()


        global count
        global a
        global counter

        pages=math.ceil(count/4)

        if(counter<=pages):
            counter+=1
            for i in range(0,4):

                if(i==0):

                    if(a>=count):
                        break;

                    f1 = Canvas(t, bd=2, bg="#CCD6FF", height=120, width=340,relief=RIDGE)
                    f1.pack(fill="both",expand="yes")
                    f1.place(x=25,y=420)
                    m = Label(f1, text=result[a][1],font=c1,bg="#CCD6FF")
                    m.place(x=5, y=5)
                    global detail1
                    detail1=result[a][1]
                    m = Label(f1, text=result[a][3],font=c2, bg="#CCD6FF",fg="grey")
                    m.place(x=5, y=27)
                    m = Label(f1, text=result[a][2],font=c2, bg="#CCD6FF",fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f1, text=result[a][4],font=c1, bg="#CCD6FF",fg="black")
                    m.place(x=290, y=40)
                    m = Label(f1, text="Prescriped:",font=c2, bg="#CCD6FF")
                    m.place(x=5, y=80)
                    m = Label(f1, text=result[a][6], bg="#CCD6FF")
                    m.place(x=70, y=80)
                    global medtype
                    medtype=result[a][6]
                    Label(f1,image=rupee1,bg="white").place(x=270,y=5)
                    m = Label(f1, text=result[a][5],font=('bold',12),fg="black", bg="white")
                    m.place(x=307, y=5)
                    spin1 = Spinbox(f1, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin1.place(x=250, y=85)
                    w=Button(f1,text="+",width=2,relief=RIDGE,bg="#CCD6FF", command=lambda: add_to_cart(result[a][1], result[a][5], int(spin1.get())))
                    w.place(x=300,y=84)

                if(i==1):

                    if(a+1>=count):
                        break;

                    f2 = Canvas(t, bd=2, bg="#EACCFF", height=120, width=340, relief=RIDGE)
                    f2.pack(fill="both", expand="yes")
                    f2.place(x=385, y=420)
                    m = Label(f2, text=result[a+1][1], font=c1, bg="#EACCFF")
                    m.place(x=5, y=5)
                    global detail2
                    detail2=result[a+1][1]
                    m = Label(f2, text=result[a+1][3], font=c2, bg="#EACCFF", fg="grey")
                    m.place(x=5, y=27)
                    m = Label(f2, text=result[a+1][2], font=c2, bg="#EACCFF", fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f2, text=result[a+1][4], font=c1, bg="#EACCFF", fg="black")
                    m.place(x=290, y=40)
                    m = Label(f2, text="Prescriped:", font=c2, bg="#EACCFF")
                    m.place(x=5, y=80)
                    m = Label(f2, text=result[a+1][6], bg="#EACCFF")
                    m.place(x=70, y=80)
                    global medtype1
                    medtype1=result[a+1][6]
                    Label(f2, image=rupee2, bg="white").place(x=270, y=5)
                    m = Label(f2, text=result[a+1][5], font=('bold', 12), fg="black", bg="white")
                    m.place(x=307, y=5)
                    spin2 = Spinbox(f2, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin2.place(x=250, y=85)
                    w = Button(f2, text="+", width=2, relief=RIDGE, bg="#EACCFF",command=lambda: add_to_cart(result[a+1][1], result[a+1][5], int(spin2.get())))
                    w.place(x=300, y=84)

                if(i==2):

                    if(a+2>=count):
                        break;

                    f3 = Canvas(t, bd=2, bg="#FFCCCC", height=120, width=340, relief=RIDGE)
                    f3.pack(fill="both", expand="yes")
                    f3.place(x=25, y=570)
                    m = Label(f3, text=result[a+2][1], font=c1, bg="#FFCCCC")
                    m.place(x=5, y=5)
                    global detail3
                    detail3=result[a+2][1]
                    m = Label(f3, text=result[a+2][3], font=c2, bg="#FFCCCC", fg="grey")
                    m.place(x=5, y=27)
                    m = Label(f3, text=result[a+2][2], font=c2, bg="#FFCCCC", fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f3, text=result[a+2][4], font=c1, bg="#FFCCCC", fg="black")
                    m.place(x=290, y=40)
                    m = Label(f3, text="Prescriped:", font=c2, bg="#FFCCCC")
                    m.place(x=5, y=80)
                    m = Label(f3, text=result[a+2][6], bg="#FFCCCC")
                    m.place(x=70, y=80)
                    global medtype2
                    medtype2=result[a+2][6]
                    Label(f3, image=rupee1, bg="white").place(x=270, y=5)
                    m = Label(f3, text=result[a+2][5], font=('bold', 12), fg="black", bg="white")
                    m.place(x=307, y=5)
                    spin3 = Spinbox(f3, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin3.place(x=250, y=85)
                    w = Button(f3, text="+", width=2, relief=RIDGE, bg="#FFCCCC",command=lambda: add_to_cart(result[a+2][1], result[a+2][5], int(spin3.get())))
                    w.place(x=300, y=84)

                if(i==3):

                    if(a+3>=count):
                        break;

                    f4 = Canvas(t, bd=2, bg="#FDDDB3", height=120, width=340, relief=RIDGE)
                    f4.pack(fill="both", expand="yes")
                    f4.place(x=385, y=570)
                    m = Label(f4, text=result[a+3][1], font=c1, bg="#FDDDB3")
                    m.place(x=5, y=5)
                    global detail4
                    detail4=result[a+3][1]
                    m = Label(f4, text=result[a+3][3], font=c2, bg="#FDDDB3", fg="grey")
                    m.place(x=5, y=27)
                    m = Label(f4, text=result[a+3][2], font=c2, bg="#FDDDB3", fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f4, text=result[a+3][4], font=c1, bg="#FDDDB3", fg="black")
                    m.place(x=290, y=40)
                    m = Label(f4, text="Prescriped:", font=c2, bg="#FDDDB3")
                    m.place(x=5, y=80)
                    m = Label(f4, text=result[a+3][6], bg="#FDDDB3")
                    m.place(x=70, y=80)
                    global medtype3
                    medtype3=result[a+3][6]
                    Label(f4, image=rupee2, bg="white").place(x=270, y=5)
                    m = Label(f4, text=result[a+3][5], font=('bold', 12), fg="black", bg="white")
                    m.place(x=304, y=5)
                    spin4 = Spinbox(f4, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin4.place(x=250, y=85)
                    w = Button(f4, text="+", width=2, relief=RIDGE, bg="#FDDDB3",command=lambda: add_to_cart(result[a+3][1], result[a+3][5], int(spin4.get())))
                    w.place(x=300, y=84)
                    Button(t, text="Next", font=c1,bg="black", fg="white", command=update_a).place(x=355, y=711)

        else:
            counter=0
            a=0
            canvas()

    # -------------------------------------------------------------

    def canvas_ayurved():

        def add_to_cart(name, price, qunt):
            total = price * qunt
            query = f"INSERT INTO temp_cart (M_name,Price,Quantity,Sub_Total) VALUES ('{name}', {price}, {qunt}, {total});"
            query1 = "UPDATE inventory SET Available = Available - %d, Sold = Sold + %d " \
                     "WHERE ID IN (" \
                     "SELECT AM_id FROM ayurvedic_med " \
                     "WHERE AM_name= '%s')" %(qunt, qunt, name)
            c.execute(query)
            c.execute(query1)
            db.commit()
            i = Label(t, text="✔ Added To Cart", font=c3, bg="black", fg="white")
            i.place(x=325, y=380)
            i.after(1200, i.place_forget)


        def destruct():
            f1.destroy()
            f2.destroy()
            f3.destroy()
            f4.destroy()

        def update_a():
            global a
            a += 4
            destruct()
            canvas_ayurved()

        global count
        global a
        global counter
        pages=math.ceil(count/4)
        if(counter<=pages):
            counter+=1
            for i in range(0,4):

                if(i==0):

                    if(a>=count):
                        break;

                    f1 = Canvas(t, bd=2, bg="#CCD6FF", height=120, width=340,relief=RIDGE)
                    f1.pack(fill="both",expand="yes")
                    f1.place(x=25,y=420)
                    m = Label(f1, text=result[a][1],font=c1,bg="#CCD6FF")
                    m.place(x=5, y=5)
                    m = Label(f1, text=result[a][3],font=c2, bg="#CCD6FF",fg="grey")
                    m.place(x=5, y=27)
                    m = Label(f1, text=result[a][2],font=c2, bg="#CCD6FF",fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f1, text=result[a][4],font=c1, bg="#CCD6FF",fg="black")
                    m.place(x=290, y=40)
                    Label(f1,image=rupee1,bg="white").place(x=270,y=5)
                    m = Label(f1, text=result[a][5],font=('bold',12),fg="black", bg="white")
                    m.place(x=307, y=5)
                    w=Button(f1,text="+",width=2,relief=RIDGE,bg="#CCD6FF", command=lambda: add_to_cart(result[a][1], result[a][5], int(spin1.get())))
                    w.place(x=300,y=84)
                    spin1 = Spinbox(f1, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin1.place(x=250, y=85)

                if(i==1):

                    if(a+1>=count):
                        break;

                    f2 = Canvas(t, bd=2, bg="#EACCFF", height=120, width=340, relief=RIDGE)
                    f2.pack(fill="both", expand="yes")
                    f2.place(x=385, y=420)
                    m = Label(f2, text=result[a+1][1], font=c1, bg="#EACCFF")
                    m.place(x=5, y=5)
                    m = Label(f2, text=result[a+1][3], font=c2, bg="#EACCFF", fg="grey")
                    m.place(x=5, y=27)
                    m = Label(f2, text=result[a+1][2], font=c2, bg="#EACCFF", fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f2, text=result[a+1][4], font=c1, bg="#EACCFF", fg="black")
                    m.place(x=290, y=40)
                    Label(f2, image=rupee2, bg="white").place(x=270, y=5)
                    m = Label(f2, text=result[a+1][5], font=('bold', 12), fg="black", bg="white")
                    m.place(x=307, y=5)
                    w = Button(f2, text="+", width=2, relief=RIDGE, bg="#EACCFF",command=lambda: add_to_cart(result[a+1][1], result[a+1][5], int(spin2.get())))
                    w.place(x=300, y=84)
                    spin2 = Spinbox(f2, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin2.place(x=250, y=85)

                if(i==2):

                    if(a+2>=count):
                        break;

                    f3 = Canvas(t, bd=2, bg="#FFCCCC", height=120, width=340, relief=RIDGE)
                    f3.pack(fill="both", expand="yes")
                    f3.place(x=25, y=570)
                    m = Label(f3, text=result[a+2][1], font=c1, bg="#FFCCCC")
                    m.place(x=5, y=5)
                    m = Label(f3, text=result[a+2][3], font=c2, bg="#FFCCCC", fg="grey")
                    m.place(x=5, y=27)
                    m = Label(f3, text=result[a+2][2], font=c2, bg="#FFCCCC", fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f3, text=result[a+2][4], font=c1, bg="#FFCCCC", fg="black")
                    m.place(x=290, y=40)
                    Label(f3, image=rupee1, bg="white").place(x=270, y=5)
                    m = Label(f3, text=result[a+2][5], font=('bold', 12), fg="black", bg="white")
                    m.place(x=307, y=5)
                    w = Button(f3, text="+", width=2, relief=RIDGE, bg="#FFCCCC",command=lambda: add_to_cart(result[a+2][1], result[a+2][5], int(spin3.get())))
                    w.place(x=300, y=84)
                    spin3 = Spinbox(f3, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin3.place(x=250, y=85)

                if(i==3):

                    if(a+3>=count):
                        f4.destroy()
                        break;

                    f4 = Canvas(t, bd=2, bg="#FDDDB3", height=120, width=340, relief=RIDGE)
                    f4.pack(fill="both", expand="yes")
                    f4.place(x=385, y=570)
                    m = Label(f4, text=result[a+3][1], font=c1, bg="#FDDDB3")
                    m.place(x=5, y=5)
                    m = Label(f4, text=result[a+3][3], font=c2, bg="#FDDDB3", fg="grey")
                    m.place(x=5, y=27)
                    m = Label(f4, text=result[a+3][2], font=c2, bg="#FDDDB3", fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f4, text=result[a+3][4], font=c1, bg="#FDDDB3", fg="black")
                    m.place(x=290, y=40)
                    Label(f4, image=rupee2, bg="white").place(x=270, y=5)
                    m = Label(f4, text=result[a+3][5], font=('bold', 12), fg="black", bg="white")
                    m.place(x=304, y=5)
                    w = Button(f4, text="+", width=2, relief=RIDGE, bg="#FDDDB3",command=lambda: add_to_cart(result[a+3][1], result[a+3][5], int(spin4.get())))
                    w.place(x=300, y=84)
                    spin4 = Spinbox(f4, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin4.place(x=250, y=85)
                    Button(t, text="Next", font=c1,bg="black", fg="white", command=update_a).place(x=355, y=711)

        else:
            counter = 0
            a = 0
            canvas_ayurved()

    # -------------------------------------------------------------

    def canvas_skin_se():

        def add_to_cart(name, price, qunt):
            total = price * qunt
            query = f"INSERT INTO temp_cart (M_name,Price,Quantity,Sub_Total) VALUES ('{name}', {price}, {qunt}, {total});"
            query1 = "UPDATE inventory SET Available = Available - %d, Sold = Sold + %d " \
                     "WHERE ID IN (" \
                     "SELECT C_id FROM care_products " \
                     "WHERE CP_name= '%s')" % (qunt, qunt, name)
            c.execute(query)
            c.execute(query1)
            db.commit()
            i = Label(t, text="✔ Added To Cart", font=c3, bg="black", fg="white")
            i.place(x=325, y=380)
            i.after(1200, i.place_forget)

        def destruct():
            f1.destroy()
            f2.destroy()
            f3.destroy()
            f4.destroy()

        def update_a():
            global a
            a += 4
            destruct()
            canvas_skin_se()

        global count
        global a
        global counter
        pages = math.ceil(count / 4)
        if (counter <= pages):
            counter += 1
            for i in range(0, 4):

                if (i == 0):

                    if (a >= count):
                        break;

                    f1 = Canvas(t, bd=2, bg="#CCD6FF", height=120, width=340, relief=RIDGE)
                    f1.pack(fill="both", expand="yes")
                    f1.place(x=25, y=420)
                    m = Label(f1, text=result[a][1], font=c1, bg="#CCD6FF")
                    m.place(x=5, y=5)
                    m = Label(f1, text=result[a][2], font=c2, bg="#CCD6FF", fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f1, text=result[a][3], font=c1, bg="#CCD6FF", fg="black")
                    m.place(x=290, y=40)
                    Label(f1, image=rupee1, bg="white").place(x=270, y=9)
                    m = Label(f1, text=result[a][4], font=('bold', 12), fg="black", bg="white")
                    m.place(x=307, y=5)
                    w = Button(f1, text="+", width=2, relief=RIDGE, bg="#CCD6FF",command=lambda: add_to_cart(result[a][1], result[a][4], int(spin1.get())))
                    w.place(x=300, y=84)
                    spin1 = Spinbox(f1, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin1.place(x=250, y=85)

                if (i == 1):

                    if (a + 1 >= count):
                        break;

                    f2 = Canvas(t, bd=2, bg="#EACCFF", height=120, width=340, relief=RIDGE)
                    f2.pack(fill="both", expand="yes")
                    f2.place(x=385, y=420)
                    m = Label(f2, text=result[a + 1][1], font=c1, bg="#EACCFF")
                    m.place(x=5, y=5)
                    m = Label(f2, text=result[a + 1][2], font=c2, bg="#EACCFF", fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f2, text=result[a + 1][3], font=c1, bg="#EACCFF", fg="black")
                    m.place(x=290, y=40)
                    Label(f2, image=rupee2, bg="white").place(x=270, y=5)
                    m = Label(f2, text=result[a + 1][4], font=('bold', 12), fg="black", bg="white")
                    m.place(x=307, y=5)
                    w = Button(f2, text="+", width=2, relief=RIDGE, bg="#EACCFF",command=lambda: add_to_cart(result[a+1][1], result[a+1][4], int(spin2.get())))
                    w.place(x=300, y=84)
                    spin2 = Spinbox(f2, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin2.place(x=250, y=85)

                if (i == 2):

                    if (a + 2 >= count):
                        break;

                    f3 = Canvas(t, bd=2, bg="#FFCCCC", height=120, width=340, relief=RIDGE)
                    f3.pack(fill="both", expand="yes")
                    f3.place(x=25, y=570)
                    m = Label(f3, text=result[a + 2][1], font=c1, bg="#FFCCCC")
                    m.place(x=5, y=5)
                    m = Label(f3, text=result[a + 2][2], font=c2, bg="#FFCCCC", fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f3, text=result[a + 2][3], font=c1, bg="#FFCCCC", fg="black")
                    m.place(x=290, y=40)
                    Label(f3, image=rupee1, bg="white").place(x=270, y=5)
                    m = Label(f3, text=result[a + 2][4], font=('bold', 12), fg="black", bg="white")
                    m.place(x=307, y=5)
                    w = Button(f3, text="+", width=2, relief=RIDGE, bg="#FFCCCC",command=lambda: add_to_cart(result[a+2][1], result[a+2][4], int(spin3.get())))
                    w.place(x=300, y=84)
                    spin3 = Spinbox(f3, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin3.place(x=250, y=85)

                if (i == 3):

                    if (a + 3 >= count):
                        break;

                    f4 = Canvas(t, bd=2, bg="#FDDDB3", height=120, width=340, relief=RIDGE)
                    f4.pack(fill="both", expand="yes")
                    f4.place(x=385, y=570)
                    m = Label(f4, text=result[a + 3][1], font=c1, bg="#FDDDB3")
                    m.place(x=5, y=5)
                    m = Label(f4, text=result[a + 3][2], font=c2, bg="#FDDDB3", fg="grey")
                    m.place(x=5, y=50)
                    m = Label(f4, text=result[a + 3][3], font=c1, bg="#FDDDB3", fg="black")
                    m.place(x=290, y=40)
                    Label(f4, image=rupee2, bg="white").place(x=270, y=5)
                    m = Label(f4, text=result[a + 3][4], font=('bold', 12), fg="black", bg="white")
                    m.place(x=304, y=5)
                    w = Button(f4, text="+", width=2, relief=RIDGE, bg="#FDDDB3",command=lambda: add_to_cart(result[a+3][1], result[a+3][4], int(spin4.get())))
                    w.place(x=300, y=84)
                    spin4 = Spinbox(f4, from_=0, to=5, width=5, bg="#F0F0F0", fg="#41440A")
                    spin4.place(x=250, y=85)
                    Button(t, text="Next", font=c1, bg="black", fg="white", command=update_a).place(x=355, y=711)

        else:
            counter = 0
            a = 0
            canvas_skin_se()

    # -------------------------------------------------------------
    # Mainpage Button Connectivity

    def med_search():
        c.execute("SELECT * FROM medicine WHERE Medicine_id LIKE 'M%'")
        global result
        result = c.fetchall()
        list(result)
        c.execute("SELECT count(Medicine_id) FROM medicine WHERE Medicine_id LIKE 'M%'")
        countlist = c.fetchone()
        list(countlist)
        global count
        global a
        global counter
        counter=1
        a=0
        count=countlist[0]
        canvas()

    def ayu_search():
        c.execute("SELECT * FROM ayurvedic_med WHERE AM_id LIKE 'A%'")
        global result
        result = c.fetchall()
        list(result)
        c.execute("SELECT count(AM_id) FROM ayurvedic_med")
        countlist = c.fetchone()
        list(countlist)
        global count
        global a
        global counter
        counter = 1
        a = 0
        count = countlist[0]
        canvas_ayurved()

    def homeo_search():
        c.execute("SELECT * FROM medicine WHERE Medicine_id LIKE 'HP%'")
        global result
        result = c.fetchall()
        list(result)
        c.execute("SELECT count(Medicine_id) FROM medicine WHERE Medicine_id LIKE 'HP%'")
        countlist = c.fetchone()
        list(countlist)
        global count
        global a
        global counter
        counter = 1
        a = 0
        count = countlist[0]
        canvas()

    def sc_search():
        c.execute("SELECT * FROM care_products WHERE C_id LIKE 'SC%'")
        global result
        result = c.fetchall()
        list(result)
        c.execute("SELECT count(C_id) FROM care_products WHERE C_id LIKE 'SC%'")
        countlist = c.fetchone()
        list(countlist)
        global count
        global a
        global counter
        counter = 1
        a = 0
        count = countlist[0]
        canvas_skin_se()

    def hh_search():
        c.execute("SELECT * FROM care_products WHERE C_id LIKE 'HH%'")
        global result
        result = c.fetchall()
        list(result)
        c.execute("SELECT count(C_id) FROM care_products WHERE C_id LIKE 'HH%'")
        countlist = c.fetchone()
        list(countlist)
        global count
        global a
        global counter
        counter = 1
        a = 0
        count = countlist[0]
        canvas_skin_se()

    def pm_search():
        c.execute("SELECT * FROM medicine WHERE Medicine_id LIKE 'PM%'")
        global result
        result = c.fetchall()
        list(result)
        c.execute("SELECT count(Medicine_id) FROM medicine WHERE Medicine_id LIKE 'PM%'")
        countlist = c.fetchone()
        list(countlist)
        global count
        global a
        global counter
        counter = 1
        a = 0
        count = countlist[0]
        canvas()

    def se_search():
        if(type==1):
            c.execute("SELECT * FROM surgical_products")
            global result
            result = c.fetchall()
            list(result)
            c.execute("SELECT count(SP_id) FROM surgical_products ")
            countlist = c.fetchone()
            list(countlist)
            global count
            global a
            global counter
            counter = 1
            a = 0
            count = countlist[0]
            canvas_skin_se()

        if(type==0):
            i=Label(t,text="Surgical Equipments not available to general customers.",font=c1,bg="black",fg="white")
            i.place(x=185,y=380)
            i.after(1200, i.place_forget)

    def gi_search():
        if(type==0):
            c.execute("SELECT * FROM general_items")
            global result
            result = c.fetchall()
            list(result)
            c.execute("SELECT count(GItem_id) FROM general_items")
            countlist = c.fetchone()
            list(countlist)
            global count
            global a
            global counter
            counter = 1
            a = 0
            count = countlist[0]
            canvas_skin_se()

        if(type==1):
            i=Label(t,text="General Items not available for hospital purchases.",font=c1,bg="black",fg="white")
            i.place(x=200,y=380)
            i.after(1200, i.place_forget)

    # --------------------------------------------------------------

    b1 = PhotoImage(file="med.png")
    Button(t, image=b1, bg="white", bd=2,relief=SOLID,command=med_search).place(x=26, y=68)
    b2 = PhotoImage(file="ay.png")
    Button(t, image=b2, bg="white", bd=2,relief=SOLID,command=ayu_search).place(x=205, y=68)
    b3 = PhotoImage(file="hp.png")
    Button(t, image=b3, bg="white", bd=2,relief=SOLID,command=homeo_search).place(x=386, y=68)
    b4 = PhotoImage(file="pc.png")
    Button(t, image=b4, bg="white", bd=2,relief=SOLID,command=pm_search).place(x=565, y=68)
    b5 = PhotoImage(file="sc.png")
    Button(t, image=b5, bg="white", bd=2,relief=SOLID,command=sc_search).place(x=26, y=223)
    b6 = PhotoImage(file="hc.png")
    Button(t, image=b6, bg="white", bd=2,relief=SOLID,command=hh_search).place(x=205, y=223)
    b7 = PhotoImage(file="s.png")
    Button(t, image=b7, bg="white", bd=2,relief=SOLID,command=se_search).place(x=386, y=223)
    b8 = PhotoImage(file="g.png")
    Button(t, image=b8, bg="white", bd=2,relief=SOLID,command=gi_search).place(x=565, y=223)

    # -------------------------------------------------------------
    t.mainloop()

# -------------------------------------------------------------


# -------------------------------------------------------------
#check func

def checklogin():
    Label(t,text="Logging In",bg="white",font=a).place(relx=0.44,rely=0.6)
    t.after(15,t.withdraw)
    t.after(15,login)

def checksign():
    Label(t,text="Creating Account",bg="white",font=a).place(relx=0.41,rely=0.6)
    t.after(15,t.withdraw)
    t.after(15,signup)

# -------------------------------------------------------------


# -------------------------------------------------------------
#signup

def signup():
    window1 = Toplevel(t)
    window1.title("Pharmacy Management System 24x7 Sign Up")
    window1.iconbitmap(r'pharmacyicon.ico')
    window1.geometry("1200x600+180+110")
    window1.resizable(width=FALSE, height=FALSE)
    c3 = Canvas(window1, width=1200, height=600)
    c3.place(x=0, y=0)
    c4 = Canvas(c3, width=850, height=450, bg="white", bd=5, relief=RAISED)
    c4.place(relx=0.5, rely=0.5, anchor=CENTER)
    c4.create_image(0, 0, image=imagepg1, anchor=NW)
    c3.create_image(0, 0, image=image1, anchor=NW)

    def back_window():
        window1.withdraw()
        main_welcome()

    def signupcust():
        global type
        type=0
        window1.withdraw()
        window5 = Toplevel(window1)
        window5.geometry("1200x600+180+110")
        window5.resizable(width=FALSE, height=FALSE)
        window5.iconbitmap(r'pharmacyicon.ico')
        c5 = Canvas(window5, width=1200, height=600)
        c5.place(relx=0.5, rely=0.5, anchor=CENTER)
        c6 = Canvas(c5, width=850, height=450, bd=5, relief=RAISED)
        c6.place(relx=0.5, rely=0.5, anchor=CENTER)
        c6.create_image(0, 0, image=image, anchor=NW)
        c5.create_image(0, 0, image=image1, anchor=NW)

        def back_window():
            window5.withdraw()
            main_welcome()

        def mp1():
            if (custefn.get() == ""):
                x=Label(c6,text="Please Enter First Name",bg="#000000",fg="#FFFFFF",font=a2)
                x.place(x=120,y=418)
                x.after(1200,x.place_forget)
            elif (custeln.get() == ""):
                x=Label(c6,text="Please Enter Last Name",bg="#000000",fg="#FFFFFF",font=a2)
                x.place(x=120,y=418)
                x.after(1200, x.place_forget)
            elif (('@' not in (custemail.get())) or ((custemail.get()).endswith('.com') == False) or ((custemail.get()).count('@') != 1)):
                x=Label(c6,text="Please Enter Email_id",bg="#000000",fg="#FFFFFF",font=a2)
                x.place(x=120,y=418)
                x.after(1200, x.place_forget)
            elif (custecno.get() == "" or len(custecno.get()) > 10 or len(custecno.get()) < 10):
                x=Label(c6,text="Contact number should be of 10 digits",bg="#000000",fg="#FFFFFF",font=a2)
                x.place(x=120,y=418)
                x.after(1200, x.place_forget)
            else:

                fn = custefn.get()
                ln = custeln.get()
                mail = custemail.get()
                cno = int(custecno.get())
                gender = v.get()
                exit=0
                while(exit==0):
                    cid=random.randrange(1100,2990,1)
                    c.execute("SELECT Customer_id FROM customer")
                    idcheck=c.fetchall()
                    list(idcheck)
                    for i in range (len(idcheck)):
                        exit=1
                        if idcheck[i][0] == cid:
                            exit=0
                sql="INSERT INTO customer (Customer_id,Customer_fn,Customer_ln,Gender,Email_id,Contact_no) VALUES (%s,%s,%s,%s,%s,%s);"
                c.execute(sql,(cid,fn,ln,gender,mail,cno))
                db.commit()
                messagebox.showwarning("IMPORTANT MESSAGE", "Your Customer Id is " + str(cid))
                window5.withdraw()
                main_welcome()

        c6.create_image(0, 0, image=imagepg3, anchor=NW)
        custefn=Entry(c6,font=b,width=16)
        custefn.place(x=215,y=100)
        custeln=Entry(c6,font=b,width=16)
        custeln.place(x=215,y=190)
        custemail=Entry(c6,font=b,width=16)
        custemail.place(x=215,y=290)
        custecno=Entry(c6,font=b,width=16)
        custecno.place(x=630,y=100)
        custrm=Radiobutton(c6,variable=v, value='m',bg="#fb9588").place(x=630,y=215)
        custrf=Radiobutton(c6, variable=v, value='f',bg="#fba28b").place(x=630,y=255)
        Button(c6, text="Submit",font=b,command=mp1,bd=5,bg="#fcb376",relief=GROOVE).place(x=680,y=340)
        Button(c6, text="Back",font=b,command=back_window,bd=5,bg="#fcb376",relief=GROOVE).place(x=580,y=340)


    def signuphos():
        global type
        type=1
        window1.withdraw()
        window6 = Toplevel(window1)
        window6.geometry("1200x600+180+110")
        window6.resizable(width=FALSE, height=FALSE)
        window6.iconbitmap(r'pharmacyicon.ico')
        c7 = Canvas(window6, width=1200, height=600, bg="#00FFFF")
        c7.place(relx=0.5, rely=0.5, anchor=CENTER)
        c8 = Canvas(c7, width=850, height=450, bg="White", bd=5, relief=RAISED)
        c8.place(relx=0.5, rely=0.5, anchor=CENTER)
        c8.create_image(0, 0, image=image, anchor=NW)
        c7.create_image(0, 0, image=image1, anchor=NW)

        def back_window():
            window6.withdraw()
            main_welcome()

        def mp2():
            if (hospen.get() == ""):
                x = Label(c8, text="Please Enter Hospital Name", bg="#000000", fg="#FFFFFF", font=a2)
                x.place(x=120, y=418)
                x.after(1200, x.place_forget)
            elif (hospern.get() == ""):
                x = Label(c8, text="Please Enter Representative Name", bg="#000000", fg="#FFFFFF", font=a2)
                x.place(x=120, y=418)
                x.after(1200, x.place_forget)
            elif (len(hosperid.get()) > 5 or len(hosperid.get()) < 5 or hosperid.get() == ""):
                x = Label(c8, text="Please Enter Representative ID", bg="#000000", fg="#FFFFFF", font=a2)
                x.place(x=120, y=418)
                x.after(1200, x.place_forget)
            elif (hospecno.get() == "" or len(hospecno.get()) > 10 or len(hospecno.get()) < 10):
                x = Label(c8, text="Contact number should be of 10 digits", bg="#000000", fg="#FFFFFF", font=a2)
                x.place(x=120, y=418)
                x.after(1200, x.place_forget)
            elif (('@' not in (hospemail.get())) or ((hospemail.get()).endswith('.com') == False) or ((hospemail.get()).count('@') != 1)):
                x = Label(c8, text="Please Enter Email_id", bg="#000000", fg="#FFFFFF", font=a2)
                x.place(x=120, y=418)
                x.after(1200, x.place_forget)
            else:
                n1 = hospen.get()
                rn1 = hospern.get()
                mail1 = hospemail.get()
                cno1 = int(hospecno.get())
                rid=int(hosperid.get())
                hgender = v.get()
                exit=0
                while(exit==0):
                    hid=random.randrange(3100,4000,1)
                    c.execute("SELECT Hospital_id FROM hospital")
                    idcheck1=c.fetchall()
                    list(idcheck1)
                    for i in range (len(idcheck1)):
                        exit=1
                        if idcheck1[i][0] == hid:
                            exit=0
                val=(hid,rn1,hgender,mail1,cno1,n1,rid)
                sql1="INSERT INTO hospital (Hospital_id,R_name,Gender,Email_id,Contact_no,Hospital_name,R_id) VALUES (%s,%s,%s,%s,%s,%s,%s);"
                c.execute(sql1,val)
                db.commit()
                messagebox.showwarning("IMPORTANT MESSAGE", "Your Hospital Id is " + str(hid))
                window6.withdraw()
                main_welcome()


        c8.create_image(0, 0, image=imagepg2, anchor=NW)
        hospen=Entry(c8,font=b,width=16)
        hospen.place(x=220,y=100)
        hospern=Entry(c8,font=b,width=16)
        hospern.place(x=220,y=265)
        hospemail=Entry(c8,font=b,width=19)
        hospemail.place(x=610,y=205)
        hospecno=Entry(c8,font=b,width=19)
        hospecno.place(x=610,y=100)
        hosperid=Entry(c8,font=b,width=16)
        hosperid.place(x=220,y=315)
        hosprm=Radiobutton(c8, variable=v, value='m', bg="#f99279").place(x=615,y=290)
        hosprf=Radiobutton(c8, variable=v, value='f', bg="#d27689").place(x=725,y=290)
        Button(c8, text="Submit",font=b,command=mp2,bg="#fcb376",bd=5,relief=GROOVE).place(x=680,y=350)
        Button(c8, text="Back",font=b,command=back_window,bg="#fcb470",bd=5,relief=GROOVE).place(x=580,y=350)

    Label(c4, text="                  Sign Up As                 ", font=a,bg="white").place(x=210, y=105)

    cust_button = Button(c4,image=cust_image,bg="white",command=signupcust)
    hos_button = Button(c4, image=hos_image,bg="white",command=signuphos)
    hos_button.place(x=505, y=165)
    cust_button.place(x=210, y=165)
    Button(c4,text="Back",bg="#fcc993",bd=5, command=back_window,font=a,relief=GROOVE).place(x=390,y=350)

# -------------------------------------------------------------


# -------------------------------------------------------------
#login

def login():
    window2=Toplevel(t)
    window2.title("Pharmacy Management System 24x7 Log In")
    window2.iconbitmap(r'pharmacyicon.ico')
    window2.geometry("1200x600+180+110")
    window2.resizable(width=FALSE, height=FALSE)
    c1 = Canvas(window2, width=1200, height=600,bg="White")
    c1.place(x=0,y=0)
    c2 = Canvas(c1, width=850, height=450, bg="White", bd=5, relief=RAISED)
    c2.place(relx=0.5, rely=0.5, anchor=CENTER)
    c2.create_image(0, 0, image=imagepg1, anchor=NW)
    c1.create_image(0, 0, image=image1, anchor=NW)

    def back_window():
        window2.withdraw()
        main_welcome()



    def logincust():
        global type
        type=0
        window2.withdraw()
        window3 = Toplevel(t)
        window3.geometry("1200x600+180+110")
        window3.iconbitmap(r'pharmacyicon.ico')
        window3.resizable(width=FALSE, height=FALSE)
        s = StringVar()
        c11 = Canvas(window3, width=1200, height=600, bg="White")
        c11.place(relx=0.5, rely=0.5, anchor=CENTER)
        c12 = Canvas(c11, width=850, height=450, bg="White", bd=5, relief=RAISED)
        c12.place(relx=0.5, rely=0.5, anchor=CENTER)
        c12.create_image(0, 0, image=image, anchor=NW)
        c11.create_image(0, 0, image=image1, anchor=NW)


        def back_window():
            t.withdraw()
            window2.withdraw()
            window3.withdraw()
            main_welcome()

        window3.minsize(1200, 600)
        c12.create_image(0, 0, image=imagepg5, anchor=NW)
        e1 = Entry(c12, font=a)
        e1.place(relx=0.61, rely=0.27, anchor=N)


        def Customer_id():
            cfn = (e2.get())
            sql = "SELECT Customer_id FROM customer WHERE Customer_fn = %s"
            x = (cfn,)
            c.execute(sql, x)
            z2 = int(e1.get())
            z1 = c.fetchall()
            list(z1)
            global custid
            custid=z2
            for i in range (len(z1)):

                if (z1[i][0] == z2):
                    window3.withdraw()
                    mp()

                else:
                    x=Label(c12, text="Not Registered",bg="#000000",fg="#FFFFFF",font=a2)
                    x.place(relx=0.43,rely=0.82)
                    x.after(1200,x.place_forget)

        def Customer_id1(e):
            Customer_id()
        e2 = Entry(c12, font=a)
        e2.bind("<Return>",Customer_id1)
        e2.place(relx=0.61, rely=0.40, anchor=N)
        Button(c12, text="Submit", command=Customer_id,font=a,bd=5,bg="#fcb376",relief=GROOVE).place(relx=0.58,rely=0.55,anchor=N)
        Button(c12, text="Back", command=back_window,font=a,bd=5,bg="#fcc993",relief=GROOVE).place(relx=0.46,rely=0.55,anchor=N)

    def loginhos():
        global type
        type=1
        window2.withdraw()
        window4 = Toplevel(t)
        window4.geometry("1200x600+180+110")
        window4.iconbitmap(r'pharmacyicon.ico')
        window4.resizable(width=FALSE, height=FALSE)
        s = StringVar()
        c13 = Canvas(window4, width=1200, height=600, bg="White")
        c13.place(relx=0.5, rely=0.5, anchor=CENTER)
        c14 = Canvas(c13, width=850, height=450, bg="White", bd=5, relief=RAISED)
        c14.place(relx=0.5, rely=0.5, anchor=CENTER)
        c14.create_image(0, 0, image=image, anchor=NW)
        c13.create_image(0, 0, image=image1, anchor=NW)

        def back_window():
            t.withdraw()
            window2.withdraw()

            window4.withdraw()
            main_welcome()

        window4.minsize(1200, 600)
        c14.create_image(0, 0, image=imagepg4, anchor=NW)
        e1=Entry(c14,font=a)
        e1.place(relx=0.58,rely=0.28,anchor=N)

        def Hospital_id():
            hid=int(e1.get())
            sql="SELECT R_id FROM hospital WHERE Hospital_id = %s"
            x=(hid,)
            c.execute(sql,x)
            z1=c.fetchone()
            list(z1)
            z2=int(e2.get())
            global hopid
            hopid=int(e1.get())
            if(z1[0]==z2):
                window4.withdraw()
                mp()
            else:
                x=Label(c14, text="Not Registered",bg="#000000",fg="#FFFFFF",font=a2)
                x.place(relx=0.43,rely=0.82)
                x.after(1200,x.place_forget)

        def Hospital_id1(e):
            Hospital_id()

        e2 = Entry(c14, font=a)
        e2.bind("<Return>", Hospital_id1)
        e2.place(relx=0.58, rely=0.41, anchor=N)
        Button(c14, text="Submit", command=Hospital_id,font=a,bd=5,bg="#fcb376",relief=GROOVE).place(relx=0.58,rely=0.55,anchor=N)
        Button(c14, text="Back", command=back_window,font=a,bd=5,bg="#fcc993",relief=GROOVE).place(relx=0.46,rely=0.55,anchor=N)

    Label(c2, text="                   Log In As                  ", bg="white", font=a).place(x=210, y=105)
    cust_button = Button(c2, image=cust_image, bg="white", command=logincust)
    hos_button = Button(c2, image=hos_image, bg="white", command=loginhos)
    hos_button.place(x=505, y=165)
    cust_button.place(x=210, y=165)
    window2.minsize(1200, 600)
    Button(window2, text="Back",bg="#fcc993",bd=5, command=back_window,font=a,relief=GROOVE).place(x=550,y=410)

# -------------------------------------------------------------


# -------------------------------------------------------------

def main_welcome():
    t = Toplevel()
    v = IntVar()
    t.title("Pharmacy Management System 24x7")
    t.iconbitmap(r'pharmacyicon.ico')
    t.resizable(width=FALSE, height=FALSE)
    t.geometry("1200x600+180+110")

    # -------------------------------------------------------------
    # check func

    def checklogin():
        Label(t, text="Logging In", bg="white", font=a).place(relx=0.44, rely=0.6)
        t.after(15, t.withdraw)
        t.after(15, login)

    def checksign():
        Label(t, text="Creating Account", bg="white", font=a).place(relx=0.42, rely=0.6)
        t.after(15, t.withdraw)
        t.after(15, signup)

    # -------------------------------------------------------------

    c1 = Canvas(t, width=1200, height=600)
    c1.place(relx=0.5, rely=0.5, anchor=CENTER)
    c2 = Canvas(c1, width=850, height=450, bd=5, relief=RAISED)
    c2.place(relx=0.5, rely=0.5, anchor=CENTER)
    image2 = PhotoImage(file="boxbg1.png")
    c2.create_image(0, 0, image=image2, anchor=NW)
    image1 = PhotoImage(file="a1.png")
    c1.create_image(0, 0, image=image1, anchor=NW)
    l_title = Label(c2, text="Pharmacy Management System", bg="#FFFFFF", fg="#000000")
    l_title['font'] = font
    l_title.place(relx=0.5, rely=0.35, anchor=CENTER)
    b_login = Button(c2, text="Log In", bg="white",fg="black",activeforeground="green",activebackground="grey",bd=1, command=checklogin,relief=RAISED)
    b_login['font'] = a
    b_login.place(relx=0.4, rely=0.53, anchor=CENTER)
    b_signup = Button(c2, text="Sign Up",  bg="white",fg="black",activeforeground="green",activebackground="grey",bd=1, command=checksign,relief=RAISED)
    b_signup['font'] = a
    b_signup.place(relx=0.6, rely=0.53, anchor=CENTER)

    t.mainloop()

# -------------------------------------------------------------


c1=Canvas(t,width=1200,height=600)
c1.place(relx=0.5,rely=0.5,anchor=CENTER)
c2 = Canvas(c1, width=850, height=450,bd=5,relief=RAISED)
c2.place(relx=0.5,rely=0.5,anchor=CENTER)
c2.create_image(0,0,image=image2,anchor=NW)
c1.create_image(0,0,image=image,anchor=NW)
l_title = Label(c2, text="Pharmacy Management System", bg="#FFFFFF", fg="#000000")
l_title['font']=font
l_title.place(relx=0.5,rely=0.35,anchor=CENTER)
b_login = Button(c2, text="Log In",bg="white",fg="black",activeforeground="green",activebackground="grey",bd=1, command=checklogin,relief=RAISED)
b_login['font']=a
b_login.place(relx=0.4,rely=0.53,anchor=CENTER)
b_signup = Button(c2, text="Sign Up",bg="white",fg="black",activeforeground="green",activebackground="grey",bd=1, command=checksign,relief=RAISED)
b_signup['font']=a
b_signup.place(relx=0.6,rely=0.53,anchor=CENTER)

t.mainloop()

# -------------------------------------------------------------