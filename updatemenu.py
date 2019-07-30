from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview
from tkinter.messagebox import  *
from connection import *



class updatemenu:

    def fullDataFetchQuery(self):
        cur = con.cursor()
        query="select * from menu"

        cur.execute(query)

        self.data=cur.fetchall()
        print(self.data)

        self.list=[]

        for i in self.data:
            self.list.append(i[1])


    def update(self):
        print("Update1")
        cur=con.cursor()
        query = 'update menu set name="' + self.itembox.get() + '",description="' + self.descbox.get(0.0,END) + '",price=' + self.pricebox.get()
        print(query)
        con.commit()
        showinfo("Message","DATA UPDATE")
        print("Update2")


    def reset(self):
        self.itembox.delete(0,500)
        self.descbox.delete(0.0, 500.0)
        self.pricebox.delete(0, 100)




    def getdetail(self):

        self.reset()
        cb=self.combobox.get()
        cur=con.cursor()
        query="select * from menu where name='"+cb+"'"
        cur.execute(query)
        data=cur.fetchone()
        print(data[1])

        print(data[3])


        # self.itembox.insert(0,data[0][1])
        print("data")
        print(data)
        self.pricebox.insert(0,data[3])
        self.itembox.insert(0,data[1])

        self.descbox.insert(0.0,str(data[2]))
        print(data[2])


    def __init__(self):
        self.window=Tk()
        self.window.title("UPDATE MENU")
        self.window.geometry("900x800")

        self.window.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")

        self.fullDataFetchQuery()
        self.select=Label(self.window,text="SELECT MENU", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.item = Label(self.window, text="ITEM NAME", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.description = Label(self.window, text="DESCRIPTION", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.price = Label(self.window, text="PRICE", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))




        self.combobox=Combobox(self.window,values=self.list,state="readonly")
        self.combobox.grid(row=0,column=0)

        self.getdetail=Button(self.window, text="GET DETAILS",command=self.getdetail)



        self.itembox=Entry(self.window)
        self.descbox=Text(self.window)
        self.pricebox=Entry(self.window)



        self.updatebttn=Button(self.window,text="update",command=self.update)







        # ''''''''griding''''



        self.select.grid(row=0,column=0)

        self.item.grid(row=1,column=0)

        self.description.grid(row=2,column=0)

        self.price.grid(row=3,column=0)





        self.combobox.grid(row=0, column=1)

        self.getdetail.grid(row=0, column=2)
        self.itembox.grid(row=1,column=1)
        self.descbox.grid(row=2,column=1)
        self.pricebox.grid(row=3,column=1)


        self.updatebttn.grid(row=5,column=1)





        self.window.mainloop()

# obj=updatemenu()
