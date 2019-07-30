from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview
from tkinter.messagebox import  *


from connection import *



class entermenu:
    def reset(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)


    def searchfun(self):

        search=self.menuText.get()
        cur=con.cursor()
        query='select * from menu where name like "'+search+'%"'
        cur.execute(query)
        self.data=cur.fetchall()
        self.insertData()

    def insertData(self):

        self.reset()

        for i in range(0, len(self.data)):

         self.treeview.insert("", i, values=self.data[i])




        # ''''''''FRAME1''''


    def __init__(self):

        self.window=Tk()

        self.window.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")

        self.frame1=PanedWindow(self.window)

        self.enter=Label(self.frame1,text="ENTER MENU", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        self.menuText=Entry(self.frame1)

        self.searchbttn=Button(self.frame1,text="Search",command=self.searchfun)



        self.enter.grid(row=0,column=0)
        self.menuText.grid(row=0,column=1)
        self.searchbttn.grid(row=0,column=2)


            # ''''''''FRAME 2''''



        self.frame2=PanedWindow(self.window)

        self.treeview=Treeview(self.frame2,columns=("menuid", "name","description","price"))
        self.treeview.heading("menuid",text="MENU ID")
        self.treeview.heading("name",text="NAME")
        self.treeview.heading("description",text="DESCRIPTION")
        self.treeview.heading("price",text="PRICE")

        # for table color

        style = Style()
        style.configure("Treeview.Heading", font=("Script MT Bold", 16))
        style.configure("Treeview", font=("calibri", 13))






        self.treeview["show"]="headings"

        self.treeview.pack()






        self.frame1.pack()
        self.frame2.pack()

        self.window.mainloop()




#obj=entermenu()