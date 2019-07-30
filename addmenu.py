from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview

from tkinter.messagebox import  *
from datetime import *
from EXCELSHEET import *
from connection import *
from http.client import*



class restaurant:

    def insertdata(self):




        # ''''''''VALIDATION''''


        itemname = self.textbox1.get()
        description = self.textbox2.get(0.0,END)
        price = self.textbox3.get()

        if len(itemname)<1 or len(description)<1  or len(price)<1:

            showinfo("","INSERT THE ADD MENU FORM")
        elif not price.isnumeric():
            showinfo('','price must be numeric')

        else:
            cur = con.cursor()
            q="select * from menu where name='"+itemname+"'"
            n=cur.execute(q)
            if n>0:
                showinfo('','same menu already exists')
            else:
                query = "insert into menu values  (NULL,'" + itemname + "','" + description + "','" + price + "') "

                cur.execute(query)
                con.commit()
                showinfo("", "DATA INSERTED")















    def __init__(self):
        self.window = Tk()

        self.window.geometry("1000x900")

        self.window.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")
        self.window.title("ADD MENU")
        self.window.iconbitmap("i.ico")

        self.AddMenu = Label(self.window, text="ADD MENU", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        self.ItemName = Label(self.window, text="Item Name", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.Description = Label(self.window, text="Description", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.Price = Label(self.window, text="Price", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        self.textbox1 = Entry(self.window)
        self.textbox2 = Text(self.window)
        self.textbox3 = Entry(self.window)

        self.button = Button(self.window, text="ADD", command=self.insertdata)

        self.AddMenu.grid(row=0, column=0, padx=30, pady=30)

        self.ItemName.grid(row=1, column=0, padx=30, pady=30)
        self.Description.grid(row=2, column=0, padx=30, pady=30)
        self.Price.grid(row=3, column=0, padx=30, pady=30)

        self.textbox1.grid(row=1, column=1, padx=30, pady=30)
        self.textbox2.grid(row=2, column=1, padx=30, pady=30)
        self.textbox3.grid(row=3, column=1, padx=30, pady=30)

        self.button.grid(row=5, column=1, padx=30, pady=30)

        self.window.mainloop()


#obj=restaurant()





