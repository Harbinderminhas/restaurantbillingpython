from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview
from tkinter.messagebox import  *
from connection import *



class kitchenscreen2:
    def reset(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)




    def insertData(self):
        cur=con.cursor()
        query= "Select * from billDetails where billid='"+str(self.billId)+"'"
        cur.execute(query)
        self.data=cur.fetchall()
        print(self.data)


        for i in range(0,len(self.data)):
            self.treeview.insert("",i,values=self.data[i])





    def check(self):
        cur=con.cursor()
        query = "update bill set status='done' where billId='" + str(self.billId)+"'"
        print(query)
        cur.execute(query)
        con.commit()
        showinfo("", "Order Is Done")
        self.window.destroy()













    def __init__(self,x):
        self.window=Tk()

        self.window.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")
        self.window.title("KITCHENSCREEN 2")
        self.window.geometry("700x700")

        self.billId=x

        self.treeview=Treeview(self.window,column=("billdetailid","billid","menuid","price","quantity","total"))


        self.treeview.heading("billdetailid",text="BILL DETAIL ID")
        self.treeview.heading("billid",text="BILL ID")
        self.treeview.heading("menuid",text="MENU ID")
        self.treeview.heading("price",text="PRICE")
        self.treeview.heading("quantity",text="QUANTITY")
        self.treeview.heading("total",text="TOTAL")

        self.treeview["show"] = "headings"

        # for table color

        style = Style()
        style.configure("Treeview.Heading", font=("Script MT Bold", 16))
        style.configure("Treeview", font=("calibri", 13))

        self.treeview.grid(row=0,column=0,columnspan=7)



        self.donebttn=Button(self.window,text="DONE",command=lambda :self.check())

        self.donebttn.grid(row=6,column=1)



        self.insertData()



        self.window.mainloop()


# obj=kitchenscreen2()


