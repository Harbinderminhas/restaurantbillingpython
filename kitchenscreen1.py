from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview
from tkinter.messagebox import  *
from connection import *

from kitchenscreen2 import *



class kitchenscreen1:
    def reset(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)




    def insertData(self):
        cur=con.cursor()
        query= "Select * from bill where status='Pending'"
        cur.execute(query)
        self.data=cur.fetchall()
        print(self.data)

        for i in range(0,len(self.data)):
            self.treeview.insert("",index=i,values=self.data[i])



    def addDetail(self):
        v=self.treeview.focus()
        c=self.treeview.item(v)
        v1=c['values']
        if len(v1)>0:

            if self.treeview.item(self.treeview.focus())['values']:
                self.treeClick = self.treeview.item(self.treeview.focus())['values']
                self.buillid = self.treeClick[0]
                obj = kitchenscreen2(self.buillid)
        else:
            showinfo('','select any bill in tree view')







    def __init__(self):

        self.window=Tk()
        self.window.geometry("1200x700")
        self.window.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")
        self.window.title("KITCHENSCREEN 1")
        self.window.iconbitmap("chef.ico")


        self.treeview=Treeview(self.window,column=("billid","typeoforder","adress","modeofpayment","cashcollected","cashreturned","mobilenumber","net amount"))

        self.treeview.heading("billid",text="BILL ID")
        self.treeview.heading("typeoforder",text="TYPE OF ORDER")
        self.treeview.heading("adress", text="ADRESS")
        self.treeview.heading("modeofpayment",text="MODE OF PAYMENT")
        self.treeview.heading("cashcollected", text="CASH COLLECTED")
        self.treeview.heading("cashreturned",text="CASHRETURNED")
        self.treeview.heading("mobilenumber", text="MOBILE NUMBER")
        self.treeview.heading("net amount", text="NET AMOUNT")
        self.treeview.column("billid",width=120)
        self.treeview.column("typeoforder", width=120)
        self.treeview.column("adress", width=120)
        self.treeview.column("modeofpayment", width=120)
        self.treeview.column("cashcollected", width=120)
        self.treeview.column("cashreturned", width=120)
        self.treeview.column("mobilenumber", width=120)
        self.treeview.column("net amount", width=120)



        self.treeview["show"]="headings"

        # for table color

        style = Style()
        style.configure("Treeview.Heading", font=("Script MT Bold", 16))
        style.configure("Treeview", font=("calibri", 13))

        self.treeview.grid(row=0,column=0,columnspan=7)

        self.insertData()


        self.button=Button(self.window,text="VIEW DETAILS",command=self.addDetail)
        self.button.grid(row=7,column=2)

        self.window.mainloop()


#obj=kitchenscreen1()

