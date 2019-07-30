from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview
from tkinter.messagebox import  *
from connection import *

class staffTree:
    def reset(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)


    def delItem(self):
        v = self.treeview.focus()
        c = self.treeview.item(v)
        v1 = c['values']
        if len(v1) > 0:
            self.treeClick = self.treeview.item(self.treeview.focus())['values']
            self.email = self.treeClick[1]
            self.mobile = str(self.treeClick[2])

            confirm = askyesno("Confirmation Window", "Are You Sure To Delete?")
            if confirm:
                cur = con.cursor()
                query = 'delete from staff where email= '"+ self.email+"''
                print(query)
                cur.execute(query)
                con.commit()
                self.insertData()
                showinfo("", "Item Deleted!")
        else:
            showinfo('','select any staff first')








    def fullDataFetchQuery(self):
        cur = con.cursor()
        query = "Select * from staff"
        cur.execute(query)
        self.data = cur.fetchall()


    def insertData(self):
        self.reset()
        self.fullDataFetchQuery()
        for i in range(0, len(self.data)):
            self.treeview.insert("", i, values=self.data[i])



    def __init__(self):
        '''Treeview FUNCTION'''
        self.window=Tk()

        self.window.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")


        self.window.title("STAFF DETAILS TREE")

        self.frame1=PanedWindow(self.window)
        self.treeview = Treeview(self.frame1, columns=("Name", "Email","Mobile","Password","Type"))
        self.treeview.heading("Name", text="NAME")

        self.treeview.heading("Email", text="EMAIL")
        self.treeview.heading("Mobile", text="MOBILE")
        self.treeview.heading("Type", text="TYPE")







        # for table color


        self.treeview["show"] = "headings"

        style = Style()
        style.configure("Treeview.Heading", font=("Script MT Bold", 16))
        style.configure("Treeview", font=("calibri", 13))







        #
        # scroll=Scrollbar(self.frame1,orient="vertical",command=self.treeview.yview)
        # scroll.pack(side=RIGHT,fill=Y)
        # self.treeview.configure(yscrollcommand=scroll.set)
        self.treeview.pack()
        self.insertData()
        self.frame2=PanedWindow(self.window)
        delBtn=Button(self.frame2,text="Delete Item",command=self.delItem)
        delBtn.grid(row=0,column=0)



        self.frame1.pack()
        self.frame2.pack()


        self.window.mainloop()


#obj=staffTree()